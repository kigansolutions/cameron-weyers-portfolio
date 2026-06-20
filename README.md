# Cameron Weyers Portfolio

Static portfolio site for Cameron Weyers, focused on AI automation, agentic workflows, and business software.

## Live Sites

- Vercel: https://cameron-weyers-portfolio.vercel.app/
- GitHub Pages: https://koslovski79.github.io/cameron-weyers-portfolio/

Vercel is the primary public URL and is used in the page metadata, sitemap, robots file, and footer.

## Files

- `index.html` - main one-page portfolio
- `cameron-weyers-cv.pdf` - downloadable CV
- `favicon.svg` - browser icon
- `social-preview.svg` - Open Graph/Twitter preview image
- `robots.txt` and `sitemap.xml` - search engine hints
- `404.html` - simple not-found page
- `vercel.json` - forces Vercel to treat the repo as a static site

## Local Preview

Open `index.html` directly in a browser, or run a tiny local server from this folder:

```bash
python -m http.server 8000
```

Then open:

```text
http://localhost:8000
```

## Deployment

The GitHub repository is connected to Vercel. Any push to `main` automatically redeploys the production site.

For a manual production deploy from this folder:

```bash
NODE_OPTIONS="--use-system-ca" vercel --prod
```

The `NODE_OPTIONS` setting is needed on this machine because the local Node/npm TLS setup needs access to the Windows system certificate store.
