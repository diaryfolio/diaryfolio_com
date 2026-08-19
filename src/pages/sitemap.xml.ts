import { getCollection } from 'astro:content';

export async function GET({ site }: { site: URL }) {
  const posts = await getCollection('posts');
  const base = site ?? new URL('https://diaryfolio.com');
  const urls = ['/', '/archive.html', '/search.html', '/privacy.html', ...posts.map((post) => post.data.legacy_url)].map((path) => `<url><loc>${new URL(path.slice(1), base)}</loc></url>`).join('');
  return new Response(`<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">${urls}</urlset>`, { headers: { 'Content-Type': 'application/xml; charset=utf-8' } });
}
