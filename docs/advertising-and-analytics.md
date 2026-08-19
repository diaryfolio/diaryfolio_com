# Advertising and analytics

DiaryFolio supports optional Google Analytics and one responsive Google AdSense placement. Both integrations are disabled unless their GitHub Actions repository variables are configured.

## Google Analytics

### Configure the build

In the GitHub repository, open **Settings → Secrets and variables → Actions → Variables** and add:

```dotenv
PUBLIC_GA_MEASUREMENT_ID=G-XXXXXXXXXX
```

Use a repository variable, not a secret or a `github-pages` environment variable. The build job reads `vars.PUBLIC_GA_MEASUREMENT_ID`. Run **Deploy to GitHub Pages** again after adding or changing the variable.

The measurement ID is intentionally public in generated client-side code. Never place an API credential or account password in a `PUBLIC_*` variable.

### Consent behaviour

When the measurement ID exists, the site renders an analytics-only consent panel but does not place the Google script in its initial HTML. It uses basic consent mode:

- no choice: display the panel and send no analytics request;
- accepted: grant `analytics_storage`, keep all advertising consent denied, and load GA4;
- rejected: remember the rejection and do not load GA4; and
- withdrawn: update consent to denied when Analytics is present, remove accessible `_ga` cookies, and reload without GA4.

The choice is stored in local storage under `diaryfolio-consent-v1` for up to 180 days. The footer Cookie settings button reopens the panel at any time. `/privacy.html` explains the behaviour to visitors.

For local testing, use an uncommitted `.env` file or pass the variable to the build:

```bash
PUBLIC_GA_MEASUREMENT_ID=G-TEST12345 npm run build
npm run preview
```

Before acceptance, confirm there is no request to `googletagmanager.com` or `google-analytics.com` and no `_ga` cookie. Test acceptance, rejection, a subsequent page load, withdrawal through the footer, keyboard focus, and a narrow viewport. Google Tag Assistant can verify consent signals against the real measurement ID after deployment.

## Google AdSense

The built-in consent panel covers Analytics only. It does not grant advertising storage, user-data, or personalisation consent and is not a substitute for a Google-certified consent-management platform.

Before enabling AdSense:

1. Add `diaryfolio.com` in Google AdSense and complete its review.
2. Create a responsive Display ad unit and copy its numeric ad-slot ID.
3. Configure an appropriate certified CMP through AdSense **Privacy & messaging** for UK, EEA, and Swiss traffic.
4. Update the privacy information and test advertising consent separately.
5. Add the exact `ads.txt` line supplied by AdSense.

Only after those steps, add GitHub Actions repository variables:

```dotenv
PUBLIC_ADS_ENABLED=true
PUBLIC_ADSENSE_CLIENT=ca-pub-XXXXXXXXXXXXXXXX
PUBLIC_ADSENSE_ARTICLE_SLOT=1234567890
```

AdSense renders only when all required values are present. Its responsive placement appears once at the end of article pages and does not appear on the homepage, archive, search, or privacy page.
