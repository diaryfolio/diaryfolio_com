import { getCollection } from 'astro:content';

const stripMarkup = (value: string) => value
  .replace(/<(script|style)[^>]*>[\s\S]*?<\/\1>/gi, ' ')
  .replace(/<[^>]+>/g, ' ')
  .replace(/&[a-z0-9#]+;/gi, ' ')
  .replace(/\s+/g, ' ')
  .trim();

export async function GET() {
  const posts = (await getCollection('posts'))
    .sort((a, b) => Date.parse(b.data.date) - Date.parse(a.data.date))
    .map((post) => ({
      title: post.data.title,
      url: post.data.legacy_url,
      date: post.data.date,
      labels: post.data.labels,
      description: post.data.description ?? '',
      text: stripMarkup(post.body ?? '')
    }));

  return new Response(JSON.stringify(posts), {
    headers: {
      'Content-Type': 'application/json; charset=utf-8',
      'Cache-Control': 'public, max-age=3600'
    }
  });
}
