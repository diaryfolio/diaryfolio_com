---
title: "Intranet Single SignOn (SSO) and Trusted URIs for locked Firefox"
date: "2014-02-17T13:00:00Z"
updated: "2014-11-21T20:28:29.066Z"
legacy_url: "/2014/02/intranet-single-signon-sso-and-trusted.html"
source_id: "tag:blogger.com,1999:blog-5931535581904587661.post-7960381464686102252"
author: "df"
labels:
  - "intranet"
  - "Technology"
  - "sso"
---

<div dir="ltr" trbidi="on">
Firefox can be customised to any extend using config files. Hence your corporate admin would be playing with<a href="http://support.mozilla.org/en-US/questions/971481" target="_blank"> certain files as mentioned in this post</a>&nbsp;(and <a href="http://kb.mozillazine.org/Locking_preferences" target="_blank">this</a>). In Summary, they edit&nbsp;"local-settings.js" or "channel-prefs.js" file. They add an entry to link to a mozilla.cfg file (or any config file), to put all the settings.<br />
<pre>pref("general.config.filename", "mozilla.cfg");</pre>
<br />
You could manipulate the "mozilla.cfg" file of your own (but next update from your company would wipe it down) or override those updates.<br />
<br />
A &nbsp;simple way to update &amp; enable Single Sign-on on my Company's internally locked firefox. &nbsp;Steps to follow..<br />
<pre>about:config</pre>
<br />
Search and add/edit following<br />
<pre>"network.negotiate-auth.trusted-uris" =&nbsp; "google.com,sso.department.abcd.com:443"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; #&lt;list of your exceptions comma separated&gt;
 "network.negotiate-auth.delegation-uris" =&nbsp; "google.com,sso.department.abcd.com:443"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; #&lt;list of your exceptions comma separated&gt;
 "network.automatic-ntlm-auth.trusted-uris" =&nbsp; "google.com,sso.department.abcd.com:443"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; #&lt;list of your exceptions comma separated&gt;</pre>
<br />
<pre>"network.websocket.enabled", false
 "signon.autologin.proxy", true</pre>
</div>
