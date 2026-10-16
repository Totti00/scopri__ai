// Scaffolds a new carousel from the skill template: carousels/<slug>/ with engine, export scripts,
// the brand logo kit and a package.json. Installs the shared dependencies once at the project root.
// Usage: node .claude/skills/scopri-carousel/scripts/new-carousel.mjs <slug> [--title "Titolo"] [--format static|animated]
import { cp, mkdir, readFile, writeFile, copyFile } from 'node:fs/promises';
import { existsSync } from 'node:fs';
import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import path from 'node:path';

const skill = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const root = path.resolve(skill, '../../..');          // project root: <root>/.claude/skills/scopri-carousel
const args = process.argv.slice(2);
const opt = (k, d) => { const i = args.indexOf(k); return i >= 0 ? args.splice(i, 2)[1] : d; };
const title = opt('--title', null), format = opt('--format', 'static');
const slug = args[0];
if (!slug || !/^[a-z0-9-]+$/.test(slug)) { console.error('Usage: new-carousel.mjs <slug-in-kebab-case> [--title "..."] [--format static|animated]'); process.exit(1); }
if (!['static', 'animated'].includes(format)) { console.error('--format must be static or animated'); process.exit(1); }
const dest = path.join(root, 'carousels', slug);
if (existsSync(dest)) { console.error(`${path.relative(root, dest)} already exists: edit it instead of re-scaffolding.`); process.exit(1); }

const tpl = path.join(skill, 'assets', 'template');
await mkdir(dest, { recursive: true });
await cp(path.join(tpl, 'engine'), path.join(dest, 'engine'), { recursive: true });
for (const f of ['export.mjs', 'export-video.mjs']) await copyFile(path.join(tpl, f), path.join(dest, f));
const html = (await readFile(path.join(tpl, 'index.html'), 'utf8'))
  .replaceAll('__TITLE__', title || slug.replace(/-/g, ' ')).replaceAll('__FORMAT__', format);
await writeFile(path.join(dest, 'index.html'), html);

// Brand logo kit: the project copy is the source of truth, the skill copy is the fallback
const kitProject = path.join(root, 'assets', 'brand', 'logo', 'kit'), kitSkill = path.join(skill, 'assets', 'brand');
const kit = existsSync(path.join(kitProject, 'scopri-ai-logo-colore.png')) ? kitProject : kitSkill;
await mkdir(path.join(dest, 'brand'), { recursive: true });
for (const v of ['negativo', 'colore', 'bianco']) await copyFile(path.join(kit, `scopri-ai-logo-${v}.png`), path.join(dest, 'brand', `scopri-ai-logo-${v}.png`));

const scripts = path.relative(dest, path.join(skill, 'scripts')).split(path.sep).join('/');
await writeFile(path.join(dest, 'package.json'), JSON.stringify({
  name: `scopri-ai-${slug}`, private: true, type: 'module',
  scripts: {
    export: 'node export.mjs',
    'export:video': 'node export-video.mjs',
    previews: `python ${scripts}/previews.py .`,
    publish: `python ${scripts}/publish-pack.py .`,
  },
}, null, 2) + '\n');
await writeFile(path.join(dest, 'copy.md'), `# ${title || slug}\n\nFormat: ${format}\n\n<!-- Approved copy goes here, slide by slide, plus caption, alt text and pinned comments. -->\n`);

// Shared dependencies live once at the project root (Node resolves them from every carousel and from the skill)
const rootPkg = path.join(root, 'package.json');
if (!existsSync(rootPkg)) await writeFile(rootPkg, JSON.stringify({ name: 'carousel-system', private: true, type: 'module' }, null, 2) + '\n');
const npm = (...a) => spawnSync('npm', a, { cwd: root, stdio: 'inherit', shell: process.platform === 'win32' });
if (!existsSync(path.join(root, 'node_modules', 'puppeteer-core'))) npm('install', 'puppeteer-core@24', '--no-fund', '--no-audit');
if (format === 'animated' && spawnSync('ffmpeg', ['-version']).status !== 0 && !existsSync(path.join(root, 'node_modules', 'ffmpeg-static')))
  npm('install', 'ffmpeg-static@5', '--no-fund', '--no-audit');

console.log(`\nCreated ${path.relative(root, dest)} (${format}).
  1. Put the approved copy in copy.md.
  2. Edit index.html: keep the layouts you need, replace the sample copy, set modes and the thread table in CAROUSEL.
  3. cd ${path.relative(root, dest)} && npm run export${format === 'animated' ? ' && npm run export:video' : ''} && npm run previews
  4. Write publish.json, then npm run publish.`);
