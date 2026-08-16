---
title: "How to revert back to google docs from google drive?"
date: "2012-07-18T08:45:00Z"
updated: "2014-06-22T17:25:40.805Z"
legacy_url: "/2012/07/how-to-revert-back-to-google-docs-from.html"
source_id: "tag:blogger.com,1999:blog-5931535581904587661.post-5252324066058369359"
author: "df"
labels:
  - "docs.google.com"
  - "google drive"
  - "Technology"
  - "corporate firewall"
  - "google drive to google docs"
---

Many of us must have faced issues of corporate firewall blocking URL's like drive.google.com, dropbox etc.<br/>I changed from google docs to google drive recently and found that my company have blocked "drive.google.com".<br/>Whatever you try, google redirects your URL to "drive.google.com" and there is NO HELP from our network adminstrator.<br/><br/>My scenario is<br/>1. Google Drive -&gt; blocked<br/>2. Google docs (docs.google.com) -&gt; OK<br/>3. Google won't allow to switch back to old google docs URL  (Hence using Temporarily classic looks fails) !!<br/><br/>I couldn't find a technical solution yet. But found a workaround ..<br/><strong>a) </strong><br/><ul><br/>	<li>Create a new gmail address or use another gmail address but DO NOT enable google Drive. Hence use old google docs in that.  (let's say  <strong>SECONDACC</strong>)</li><br/>	<li>From your original (problem facing) google drive, create a new folder and share the folder and its contents with <strong>SECONDACC</strong> . This needs to be done at somewhere you have complete access outside corporate firewall.</li><br/>	<li>Ensure <strong>SECONDACC</strong> have full access and hence you can modify from <strong>SECONDACC</strong> docs</li><br/></ul><br/><strong>b)</strong> You can still access a file if you know the URL.  i.e. Even if you have enabled Google Drive, the URL for a file or spreadsheet still points to docs.google.com<br/>Something like...<br/><ul><br/>	<li>https://docs.google.com/spreadsheet/ccc?key=abcefghijklml#gid=9   OR</li><br/>	<li>https://docs.google.com/folder/d/xxxxxxxxxxxxxxxxxx/edit</li><br/></ul><br/>Hence note down the file key and access it directly.<br/><br/>C) Waiting for other options !!
