---
title: "cURL-Siteminder Automation (Automating Authentication)"
date: "2013-08-20T15:22:00Z"
updated: "2014-11-20T23:59:14.717Z"
legacy_url: "/2013/08/curl-siteminder-automation-automating.html"
source_id: "tag:blogger.com,1999:blog-5931535581904587661.post-6652573803693454629"
author: "df"
labels:
  - "Technology"
---

<div dir="ltr" trbidi="on">
I have discovered that cURL is intelligent than humans !! cURL is surrounded by a huge list of command-line options which makes it even powerful than browser itself<br />
<h2>
Scenario in our company</h2>
<ul><br />
<li>Siteminder protects web-pages and web-services under particular FQDN/realm</li>
<br />
<li>Siteminder integrates with SSO/LDAP. Hence a Userid/Password is always displayed when u enter our FQDN</li>
<br />
<li>We wanted to automate data collection and measurement via automated mechanism and cannot bypass siteminder security</li>
</ul>
<br />
<h2>
Some Definitions</h2>
<br />
<strong>Siteminder Realm</strong> - A domain which shares an authentication database and servers. There is a single name-space for principal name/instance pairs within a realm. A realm is also a logical collection of clients and servers registered in the database.<br />
<strong>SSO</strong> - Single Sign-on by various mechanisms. We had One time password (OTP) also in our devices which needs manual entry as its tied to a human user.<br />
<h2>
How it can be achieved</h2>
<ul><br />
<li>cURL can do the magic !! Install cURL (hopefully most of *NIX systems have cURL installed) and put into your classpath</li>
<br />
<li>When a request is received at FQDN, Siteminder asks you to authenticate</li>
<br />
<li>You will Notice that the URL you entered have changed and is a very long URL now !!</li>
<br />
<li>If you carefully look the URL,&nbsp; it shows the URL has a "Target" component which would be the landing page it would redirect after successful login</li>
<br />
<li>The idea is to grab the "Target" URL, the cookie headers &amp; put in the credentials as a config file.</li>
</ul>
<br />
<pre>eg RequstURL = https://diaryfolio.com:443/webServices/signon 
userID = diaryfolio 
passWord = test</pre>
<br />
<br />
<pre>Fetch the URI for login 
authenticationPageURI=`curl -s -I --cookie-jar tmpCookieFile --cookie tmpCookieFile --insecure ${RequstURL} | grep Location| sed "s/Location: //g"`</pre>
<br />
Carefully look into this "authenticationPageURI" variable and determine where is your "Target" location starts eg<br />
<pre>https://diaryfolio.com:443/LoginPage/?myCustomTarget=https%3A%2F%diaryfolio%3A443%2FwebServices%2Fsignon%3Floc%3DZ2thgRC3_-L_w0YbyB6qaOe4Am2gKkrZPw8vQLD_4yY</pre>
<br />
<pre>targetURI=`echo $authenticationPageURI | sed 's/^.*\?myCustomTarget=/\?myCustomTarget=/'`
 fullTargetURI=${RequstURL}"/addExtraVariablesIfYouHave/"${targetURI}&nbsp; # This will be your whole URL</pre>
<br />
This extracts the target URI<br />
<br />
<br />
Now extract the cookie data into a file&nbsp; (<strong>tmpDiaryFolioCookieFile</strong>)<br />
<pre>curl -s --insecure --cookie-jar tmpDiaryFolioCookieFile --cookie tmpDiaryFolioCookieFile --location --data "user=${userID}&amp;pass=${passWord}" ${fullTargetURI} &gt; webServiceData.xml</pre>
<br />
Now using this tmpDiaryFolioCookieFile, we will play.<br />
<pre>#Delete a web-service function. It is your function 
curl -s -L --insecure --cookie-jar tmpDiaryFolioCookieFile --cookie tmpDiaryFolioCookieFile "${fullTargetURI}"/webServices/delete/myWebService &gt;/dev/null</pre>
<br />
<pre>#Import a web-service. It is your function 
curl -s -L --insecure --cookie-jar tmpDiaryFolioCookieFile --cookie tmpDiaryFolioCookieFile -F uploadFile=webServiceData.xml "${fullTargetURI}"/webServices/import</pre>
<br />
</div>
