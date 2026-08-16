import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://diaryfolio.com',
  trailingSlash: 'never',
  build: { format: 'file' }
});
