# Advertising and analytics

DiaryFolio supports Google Analytics and one responsive Google AdSense placement at the end of each article. Both integrations are disabled unless their build variables are configured.

## Before enabling AdSense

1. Add the production site domain (for example, `diaryfolio.com`) in Google AdSense and complete its review.
2. Create a responsive Display ad unit in **Ads → By ad unit** and copy its numeric ad-slot ID.
3. Configure a consent message in AdSense **Privacy & messaging** before serving advertising to visitors in the UK, EEA, or Switzerland. Google requires a certified CMP integrated with the IAB TCF for relevant advertising traffic. Publish a privacy and cookie notice that explains Google Analytics, AdSense, and how visitors can change their choices.

## Cloudflare Workers Builds configuration

In Cloudflare, open **Workers & Pages → the DiaryFolio Worker → Settings → Build → Build Variables and Secrets**. Add these as plaintext **Build Variables**, then trigger a new build:

```dotenv
# Google Analytics; omit this line to disable Analytics entirely.
PUBLIC_GA_MEASUREMENT_ID=G-XXXXXXXXXX

# Google AdSense; omit or set PUBLIC_ADS_ENABLED=false to disable ads entirely.
PUBLIC_ADS_ENABLED=true
PUBLIC_ADSENSE_CLIENT=ca-pub-XXXXXXXXXXXXXXXX
PUBLIC_ADSENSE_ARTICLE_SLOT=1234567890
```

These are build-time settings, not Worker runtime variables. Astro resolves `PUBLIC_*` values while running `npm run build`; the resulting values are included in the public HTML. Do not store API credentials, account passwords, or any other private value in them.

For local testing, put the same values in an uncommitted `.env` file and run `npm run build`.

## What the site renders

- When `PUBLIC_GA_MEASUREMENT_ID` is set, the shared layout emits the Google Analytics tag on every generated page.
- AdSense is rendered only when `PUBLIC_ADS_ENABLED=true`, `PUBLIC_ADSENSE_CLIENT`, and `PUBLIC_ADSENSE_ARTICLE_SLOT` are all set.
- The ad appears once, at the end of article pages. It does not appear on the homepage, archive, or search page.

After deployment, inspect the HTML source of an article to confirm the Google tag and AdSense client/slot values are present. Ads may not show until AdSense has approved the site and ad unit.
