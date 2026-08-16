import { getCollection } from 'astro:content';

export async function GET({ site }: { site: URL }) {
  const posts = (await getCollection('posts')).sort((a, b) => Date.parse(b.data.date) - Date.parse(a.data.date));
  const base = site ?? new URL('https://diaryfolio.com');
  const items = posts.map((post) => `<item><title><![CDATA[${post.data.title}]]></title><link>${new URL(post.data.legacy_url.slice(1), base)}</link><guid>${new URL(post.data.legacy_url.slice(1), base)}</guid><pubDate>${new Date(post.data.date).toUTCString()}</pubDate><description><![CDATA[${post.data.description ?? ''}]]></description></item>`).join('');
  return new Response(`<?xml version="1.0" encoding="UTF-8" ?><rss version="2.0"><channel><title>DiaryFolio</title><link>${base}</link><description>Technology notes, guides, and experiments.</description>${items}</channel></rss>`, { headers: { 'Content-Type': 'application/xml; charset=utf-8' } });
}
