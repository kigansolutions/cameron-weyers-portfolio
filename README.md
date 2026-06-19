# Cameron Weyers — Portfolio

A single-page static portfolio site. No build step, no dependencies — just HTML/CSS.

## Files

- `index.html` — the entire site (styles are inline in a `<style>` block)
- `cameron-weyers-cv.pdf` — linked by the "Download CV" button

## Preview locally

Open `index.html` directly in a browser, or serve the folder:

```bash
python -m http.server 8000
# then visit http://localhost:8000
```

## Deploy

This is a static site — it works on any static host.

**Netlify / Vercel / Cloudflare Pages:** drag-and-drop this folder, or point the
project at it. No build command; the publish/output directory is the folder root.

**GitHub Pages:** push this folder to a repo and enable Pages on the branch root.

## Custom domain

The footer and email reference `cameronweyers.dev`. Once you own the domain,
point it at your host and the site is live. The contact email
(`cameron@cameronweyers.dev`) needs a mailbox set up at that domain to receive mail.

## Editing

Everything is in `index.html`. To swap the CV, replace `cameron-weyers-cv.pdf`
(keep the filename, or update the link in the hero button).
