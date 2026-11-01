# flanker docs

The documentation site for flanker, built with [Astro Starlight](https://starlight.astro.build)
and served at **docs.flanker.wtf** via GitHub Pages.

## Develop

```bash
npm install
npm run dev        # http://localhost:4321
```

## Command reference

The category pages under `src/content/docs/commands/` and `src/data/` are generated from the bot's
`assets/help.txt`, command registry and typed slash catalog so they stay accurate. Regenerate them (run from this folder,
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

The live repository is `shahzain345/flanker-docs`. Its `main` branch uses the
included GitHub Actions workflow to build and deploy to Pages. `public/CNAME`
preserves the `docs.flanker.wtf` custom domain.

A local build does not publish the docs. Commit and push the reviewed site
changes only when the owner has authorised that step, then verify the Pages
workflow and the changed public URLs. Do not include `.env` files, dependencies
or local build output.

## Structure

```
src/content/docs/
  index.mdx              home (splash)
  start/                 getting-started, setup
  guides/                security, moderation, logging, welcome, tickets, dashboard
  commands/              GENERATED from help.txt (do not hand-edit)
scripts/gen-commands.py  the generator
src/styles/brand.css     dashboard-matched neutral glass and Inter
src/components/          accessible setup diagrams and command references
src/data/                generated public command and typed slash data
public/CNAME             custom domain
```

## Keep published docs current

After changing bot commands, run `npm run gen` here with the current bot checkout
one directory up. Review the generated reference and update the affected setup
guides too. `npm run build` validates the site; check changed pages at desktop,
390px and 360px widths before publishing. The Pages workflow builds committed
Markdown, so changing `assets/help.txt` alone does not update the public docs.

Current setup guides include public Valorant LFG, Minecraft bridge pairing,
music and 24/7 playback, friendships and gifts, ticket access roles, leveling
role migration, security and bulk-role limits.


## Coverage and design checks

Run `npm run gen` followed by `npm run check:commands`. Generation fails when public help and the Rust registry disagree. The coverage check verifies every public root, alias data, prefix form and registered typed slash route. Internal pingtrace stays excluded. Category `.mdx` files are generated; `commands/index.mdx` is maintained by hand.

Setup illustrations are explicitly labeled examples. They show no live server state and make no Discord requests. Keep source-based behavior, prefix and actual dashboard labels current. Test search, profile filtering, native mobile navigation, keyboard focus and 360/390px layout before publication. Keep the same Inter font, neutral glass, divided rows and restrained typography as the dashboard.
