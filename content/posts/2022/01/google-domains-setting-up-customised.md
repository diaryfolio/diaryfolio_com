---
title: "Google Domains & Setting up customised email without workspace"
date: "2022-01-12T13:08:00.009Z"
updated: "2025-08-16T09:54:41.378Z"
legacy_url: "/2022/01/google-domains-setting-up-customised.html"
source_id: "tag:blogger.com,1999:blog-5931535581904587661.post-4346573342090360893"
author: "df"
labels:
  - "Domains"
  - "Web development"
---

<h2>🔍 Summary</h2>
<p>
    Google services are extremely powerful and customizable. In this guide, we'll show you how to set up:
</p>
<ul>
    <li>📥 Email forwarding from your custom domain to Gmail</li>
    <li>📤 Sending emails from your domain via Gmail using SMTP</li>
    <li>💸 All at zero cost (aside from the domain purchase)</li>
</ul>

<div>
    <img src="https://blogger.googleusercontent.com/img/a/AVvXsEi9vWHyQP55dQg0ATRp17MYIYFnXdh5g1SI6HDkA8I-q8lJZKXct88Q4loy2pF1kw7XZfZ9RTJVv-4-IBGJ_yuht0Fz_k6i_sV9ymU1iArEJDliK9ayKyA3x4Q8Exfsm9-KVV1ayEK1u3lJHmPl6heh6A4PPqb2Trz3mlepWfLUQ3kRc8QCD7RAJ_xA=s600" alt="Google Domains" width="500" />
</div>

<hr>

<h2>🛠️ Prerequisites</h2>
<ul>
    <li>✅ A custom domain (e.g. from <a href="https://domains.google" target="_blank">Google Domains</a>)</li>
    <li>✅ A Gmail account</li>
</ul>

<hr>

<h2>📩 Part 1: Email Forwarding via Google Domains</h2>

<h3>Step 1: Setup Email Forwarding</h3>
<ol>
    <li>Go to <code>https://domains.google.com/registrar/&lt;your_domain&gt;/dns</code></li>
    <li>Navigate to: <strong>Email → Email forwarding → Add email alias</strong></li>
    <li>Enter your alias (e.g. <code>admin@yourdomain.com</code>) and the Gmail address to forward to</li>
    <li>Click <strong>“Add”</strong> and verify via the email sent to your Gmail</li>
</ol>

<div>
    <img src="https://blogger.googleusercontent.com/img/a/AVvXsEiYvQ5AeGdjtePJg0jeQteDxDI2M5Af36G7QeH5rsIJIl1ROpepv1srrt4FLStvnwSCWbyQ-RWYBypcfjilNBgtgrSB2prD7uZO234EzV5kVZgRMX6r8a6JCLHyELrbzVr0_s6crvwoZdym1ot-bhWyIYx8vGdlDB08JUuejoWLOZ8xgkvvY1IzWcB2=w640-h128" width="600" />
</div>

<h3>Step 2: Verify DNS MX Records</h3>
<ol>
    <li>In Google Domains, go to <strong>DNS</strong> section</li>
    <li>Ensure the correct MX records are set (added automatically during forwarding)</li>
</ol>

<div>
    <img src="https://blogger.googleusercontent.com/img/a/AVvXsEj8OUdyOeVf6KMYXzxmH7KCNC5nRxJMrWzFB1cOpoRE-2RHE52PZhgzHezPW7pi_WXTZU5_f2540AZhQUGbOxEnKFdvPNyt6QpYuBeuvDbfrzkrDeNP5JJ_R6ehObIs9e4fQEFYRB6dGJfab6EJOm4IIzkk7VkJ3QeP0ZnNzWeaKYjWD0AryqG_yzWo=w400-h326" width="500" />
</div>

<h3>Step 3: Test Forwarding</h3>
<p>Send an email to your new domain email address (e.g. <code>admin@yourdomain.com</code>). It should land in your Gmail inbox.</p>

<hr>

<h2>📤 Part 2: Send Emails Using Gmail with Your Domain</h2>

<h3>Step 1: Generate an App Password</h3>
<ol>
    <li>Go to <a href="https://myaccount.google.com/security" target="_blank">Google Account Security</a></li>
    <li>Under <strong>“App Passwords”</strong>: Generate one for "Mail" → "Other"</li>
    <li>Copy the generated 16-character password</li>
</ol>

<div>
    <img src="https://blogger.googleusercontent.com/img/a/AVvXsEguPJavhj5FFVxREKVkGsYP0NiLNqByfJDO9KXXYqi1y7dbnfpA42xD478R0NpC1eSW0W4BaVByF-eGyZQhjxBqXrNgz-wWAOYO2J2Qyw_3DdhNGmbuPbuUBnNpUR6MpWPQi6c2iT9jBQocFyFYUauW_hdxvaAOVrg2U52Cf7520m79Fu9eXloJ0XFk=w400-h265" width="500" />
</div>

<h3>Step 2: Add Your Domain Email in Gmail</h3>
<ol>
    <li>Go to <a href="https://mail.google.com/mail/u/0/#settings/accounts" target="_blank">Gmail Settings → Accounts</a></li>
    <li>Under <strong>“Send mail as”</strong>, click <strong>“Add another email address”</strong></li>
    <li>Enter your name and custom email (e.g. <code>admin@yourdomain.com</code>)</li>
</ol>

<div>
    <img src="https://blogger.googleusercontent.com/img/a/AVvXsEh8IvyXXhDLuREUbHzAu4IlwsXok42tm2rmTy6u47TYEW2gY59rmKypUUH5z5gkDBQUEaE3SdKc5jDuks0D7uL0hw0XNMjLD84KTwL7IHEle10_vLlDJmAhAMnkGEaRw2ggno7k85IHcr1Ev-JUzqopCldn3GZFBou0036l-3QvAzLaZb0SkhBpK2rI=w400-h289" width="500" />
</div>

<h3>Step 3: Configure SMTP Settings</h3>
<ul>
    <li>SMTP Server: <code>smtp.gmail.com</code></li>
    <li>Port: <code>587</code> (TLS) or <code>465</code> (SSL)</li>
    <li>Username: your Gmail address</li>
    <li>Password: the app password you generated</li>
</ul>

<div>
    <img src="https://blogger.googleusercontent.com/img/a/AVvXsEg6aF373KnJ4bm0jisHfyLwHpcO_lAG9xUhv0S_MPTQ2nXPncNQ-wXdadouO_2BPOZhYDQujqzBXN3uSDZXz84ebxdPNNopmsmkls7GqgrH6VTbuFFA0Qc2WwBV6NL2CMG53JxpyCYPrPaCtD1D8XfDPpbR9UV-Qlz6gZEAgw2CJFLq1-MFISRORHUQ=w400-h225" width="500" />
</div>

<h3>Step 4: Confirm & Verify</h3>
<ol>
    <li>You’ll receive a verification email to your domain email address</li>
    <li>Click the link or enter the code in the Gmail popup</li>
    <li>✅ Done! Now you can choose your domain email as the “From” address when replying from Gmail</li>
</ol>

---

<h2>✅ Final Notes</h2>
<ul>
    <li>✔️ You now receive and send emails with your custom domain via Gmail</li>
    <li>✔️ Professional branding with zero email hosting cost</li>
    <li>💬 Questions? Drop them in the comments below</li>
</ul>
