# flanker docs

The documentation site for flanker, built with [Astro Starlight](https://starlight.astro.build)
and served at **docs.flanker.wtf** via GitHub Pages.

## Develop

```bash
npm install
npm run dev        # http://localhost:4321
```

## Command reference

The pages under `src/content/docs/commands/` are generated from the bot's
`assets/help.txt` so they stay accurate. Regenerate them (run from this folder,
with the bot repo checked out one level up):

```bash
npm run gen        # = python3 scripts/gen-commands.py ../assets/help.txt
```

Then commit the changed Markdown. The generator needs only Python 3.

## Build

```bash
npm run build      # outputs ./dist
npm run preview    # preview the built site
```

## Deploy to GitHub Pages at docs.flanker.wtf

One-time setup:

1. Create a GitHub repo named `flanker-docs` and push this folder to `main`.
   Update the `editLink.baseUrl` in `astro.config.mjs` (replace `REPLACE_ME`
   with your GitHub username/org), or remove that option.
2. In the repo: **Settings -> Pages -> Build and deployment -> Source: GitHub
   Actions**. The included workflow (`.github/workflows/deploy.yml`) builds and
   deploys on every push to `main`.
3. In **Settings -> Pages -> Custom domain**, enter `docs.flanker.wtf` and save,
   then tick **Enforce HTTPS** once the certificate is issued.
4. At your DNS provider for `flanker.wtf`, add a record:

   ```
   Type: CNAME
   Host/Name: docs
   Value: <your-github-username>.github.io
   ```

   (`public/CNAME` already contains `docs.flanker.wtf`, which keeps the custom
   domain across deploys.)

DNS can take a few minutes to an hour to propagate. After that, pushes to `main`
publish automatically.

## Structure

```
src/content/docs/
  index.mdx              home (splash)
  start/                 getting-started, setup
  guides/                security, moderation, logging, welcome, tickets, dashboard
  commands/              GENERATED from help.txt (do not hand-edit)
scripts/gen-commands.py  the generator
src/styles/brand.css     flanker brand accents
public/CNAME             custom domain
```
