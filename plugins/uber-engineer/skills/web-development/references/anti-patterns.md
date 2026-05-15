# Web Development — Anti-Patterns

Push back when you see these. Each one ships with a concrete fix path.

### Every page SSR'd because someone heard SSR was good.

**Fix:** Audit each route's actual data needs. Static pages should be SSG/ISR (cheap, fast). Personalized pages should be SSR or RSC. SPA only where the route is a stateful app shell. Document the choice per route.

### Client-side routing without a 404 page.

**Fix:** Add an explicit not-found route at the framework level (Next.js `not-found.tsx`, Remix `CatchBoundary`, SvelteKit `+error.svelte`). Test by hitting a deliberately broken URL — assert correct status code + helpful UI.

### Meta tags in components that don't render server-side.

**Fix:** Move SEO metadata to the framework's metadata API (Next.js `generateMetadata`, Remix `meta`, SvelteKit `<svelte:head>`). Confirm by curling the page and grep-ing for the title tag in the response — not the rendered DOM.

### Cache busting via query string instead of fingerprinted filenames.

**Fix:** Switch to content-hashed filenames at build time. Set the static asset cache to immutable, max-age=31536000. The HTML stays uncached or short-cached; it references the new fingerprinted asset on every release.

### Production deploys without preview URLs.

**Fix:** Wire per-PR preview URLs (Vercel preview deployments, Cloudflare Pages preview branches, Netlify deploy previews). Block merge until the preview renders the change. Document the preview URL in the PR description.


## How to push back

State the anti-pattern, name the specific evidence you saw, propose the minimal change, link the
official doc that justifies it. Don't moralize. Don't list every problem at once. One issue at a
time, confirm, move to the next.
