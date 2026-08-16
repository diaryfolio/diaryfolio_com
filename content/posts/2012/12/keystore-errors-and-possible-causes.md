---
title: "Keystore Errors and possible causes"
date: "2012-12-11T10:45:00Z"
updated: "2015-04-07T07:46:56.699Z"
legacy_url: "/2012/12/keystore-errors-and-possible-causes.html"
source_id: "tag:blogger.com,1999:blog-5931535581904587661.post-5456904109352780724"
author: "df"
labels:
  - "cacerts"
  - "java"
  - "keytool"
  - "Technology"
  - "trustcacerts"
  - "alias"
  - "keystore"
---

<div dir="ltr" trbidi="on">
You might have played with the keystore and java security objects many times.Some of these errors happen when you install it first time<br />
<div class="separator">
<a href="/assets/images/original/2012/12/keystore-errors-and-possible-causes/keystore_1.jpg" imageanchor="1"><img border="0" src="/assets/images/original/2012/12/keystore-errors-and-possible-causes/keystore_1.jpg" height="284" width="320" /></a></div>
<br />
<pre># Java's default cacerts password is "changeit", unless you're on a Mac, where it's "changeme".
 # Better to execute it as root, hence sudo su
 sudo su - -c /usr/java6_64/bin/keytool -import -trustcacerts -file /tmp/ServerCertficate.crt -keystore /usr/java6_64/jre/lib/security/cacerts -alias diaryfolio_Certificate</pre>
<br />
<pre>#No need of any password while viewing (Just press enter)
 /usr/java6_64/bin/keytool -list -v -keystore /usr/java6_64/jre/lib/security/cacerts&nbsp;&nbsp; &gt;/tmp/java6.abc</pre>
<h2>
Common Errors</h2>
<h3>
1. &nbsp;Keytool Error with Java lang Exception</h3>
<pre><strong>&nbsp;keytool error: java.lang.Exception: Input not an X.509 certificate</strong></pre>
<br />
This may be caused due to<br />
- Not specifying an alias name correctly?<br />
- Space or incorrect blanks<br />
- Check in the certificate (.crt file), if there are any headers or footers before<br />
<pre> —–BEGIN CERTIFICATE—–</pre>
<br />
<br />
or anyting after<br />
<pre> —–END CERTIFICATE—–</pre>
<br />
<span><strong>Solution</strong>:&nbsp;</span>Remove entries after head and footers and try importing again<br />
<h3>
&nbsp;2. &nbsp;Keytool Error with Java Filenotfound Exception</h3>
<pre><strong>keytool error (likely untranslated): java.io.FileNotFoundException: /usr/java6_64/jre/lib/security/cacerts (Permission denied)</strong></pre>
<br />
<span><strong>Solution</strong>:</span>This happens because you don't have edit permission (or insert) for the keystore. Run as root.<br />
<h3>
<span>&nbsp;3</span>. &nbsp;Keytool Error with Java IO Exception</h3>
<pre><strong>&nbsp;keytool error (likely untranslated): java.io.IOException: Keystore was tampered with, or password was incorrect</strong></pre>
<br />
<span><strong>Solution</strong></span>: Ensure the password is correct. Try &nbsp;password "<em>changeit</em>" &nbsp;(as it is the default) or the password might have been changed by someone. In which case contact your OS admin having root access and try to export the keytool entries as exporting doesn't require password. (Step at top of this page). Carefully find the entries which you feel is required for your organisation, later create a cacerts file of your own and import these custom entries.</div>
