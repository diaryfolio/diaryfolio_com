---
title: "Certification authority and applying certificate to your domain"
date: "2014-03-25T16:12:00Z"
updated: "2014-12-01T07:16:32.118Z"
legacy_url: "/2014/03/certification-authority-and-applying.html"
source_id: "tag:blogger.com,1999:blog-5931535581904587661.post-4754564583598004588"
author: "df"
labels:
  - "Technology"
  - "Aside"
---

<div dir="ltr" trbidi="on">
<div>
Generating a Certificate Signing Request and applying the certificate is&nbsp; very frequent. Some companies require 2048 bit signatures. The following steps will create certificates with 2048 bit and later apply to relevant httpd (apache) server.</div>
<div>
<br /></div>
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container"><tbody>
<tr><td><a href="/assets/images/original/2014/03/certification-authority-and-applying/certificate.jpg" imageanchor="1"><img border="0" src="/assets/images/original/2014/03/certification-authority-and-applying/certificate.jpg" height="196" width="400" /></a></td></tr>
<tr><td class="tr-caption">Certificate Hierarchy</td></tr>
</tbody></table>
<h3>
Creating a CSR</h3>
<h4>
<span>Values</span></h4>
<pre>Country Name (2 letter code) [AU]:GB
State or Province Name (full name) [Some-State]:London
Locality Name (eg, city) []:Croydon
Organization Name (eg, company) [Internet Widgits Pty Ltd]:My company
Organizational Unit Name (eg, section) []:diaryfolio.com
Common Name (eg, YOUR name) []:subdomain.diaryfolio.com
Email Address []:</pre>
<br />
<h3>
Things to remember</h3>
<ul>
<li>In most cases, ensure "Email address is left blank". But consult your certificate signing authority on this.</li>
<li>Ensure "Common Name" matches exactly the "ServerName" specified in your httpd.conf (or httpd/conf/extra/httpd-ssl.conf)</li>
</ul>
<h4>
<span>Actual Creation</span></h4>
Below creates CSR with 2048 bit<br />
<pre># CSR Key generation
# Generate a new private key and a new csr, using the default bit length.
&nbsp;openssl req -new -keyout &lt;NEWKEYFILE&gt; -out &lt;NEWCSRFILE&gt;

# Generate a new rsa 2048 key and a new CSR, using a bit length of 1024 (or other specified length).
&nbsp;openssl req -newkey rsa:2048 -keyout &lt;NEWKEYFILE&gt; -out &lt;NEWCSRFILE&gt;

# Generate a CSR based on an existing key, you'll need to know the key's passphrase. The CSR bit length is the same as the key that was used to create it.
&nbsp;openssl req -out &lt;NEWCSRFILE&gt; -key &lt;PROVKEYFILE&gt; -new

# Check a private key bit length, you'll need to know the key's passphrase.
&nbsp;openssl rsa -in 2048.key -text -noout

# Check a CSR bit length.
&nbsp;openssl req -in &lt;CSRFILENAME&gt; -text -noout | grep bit</pre>
<br />
Once you receive the .csr or .crt file from the authority, you need to apply this to your web-application.<br />
<pre>openssl, all the subcommands are listed and linked to from this man page.
https://www.openssl.org/docs/apps/openssl.html

subcommand "req" help: https://www.openssl.org/docs/apps/req.html#

subcommand "genrsa" help: https://www.openssl.org/docs/apps/genrsa.html#

subcommand "rsa" help: https://www.openssl.org/docs/apps/rsa.html#</pre>
<br />
<br />
Also remember to apply this to your <span><strong>java keystore if you are using Tomcat</strong></span><br />
<pre>#####&nbsp;&nbsp; Suppose your java location is : /usr/java6_64/
certificateFile="&lt;your_certificate_Location&gt;"
certificateElias="&lt;yourCertificateAlias&gt;"
sudo su - -c /usr/java6_64/bin/keytool -import -trustcacerts -file ${certificateFile} -keystore /usr/java6_64/jre/lib/security/cacerts -alias ${certificateElias}</pre>
<br />
If you find any Errors, <a href="https://diaryfolio.com/2012/12/keystore-errors-and-possible-causes.html" target="_blank">do check my previous post</a><br />
<h2>
OpenSSL Examples</h2>
<br />
A <a href="http://conshell.net/wiki/index.php/OpenSSL_usage_tips_and_examples" target="_blank">great document is kept here</a><br />
<h3>
View certificates details</h3>
<pre>openssl x509 -in filename.crt -noout -text</pre>
</div>
