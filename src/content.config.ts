import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

const postSchema = z.object({
  title: z.string(),
  date: z.string(),
  updated: z.string().optional(),
  legacy_url: z.string(),
  research_id: z.string().regex(/^AR_[0-9]{4,}$/).optional(),
  source_id: z.string().optional(),
  author: z.string().optional(),
  labels: z.array(z.string()).default([]),
  description: z.string().optional()
});

const posts = defineCollection({
  loader: glob({ base: './content/posts', pattern: '**/*.md' }),
  schema: postSchema
});

export const collections = { posts };
