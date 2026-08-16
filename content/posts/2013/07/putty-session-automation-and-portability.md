---
title: "Putty Session automation and portability"
date: "2013-07-12T08:46:00Z"
updated: "2015-06-03T09:32:50.928Z"
legacy_url: "/2013/07/putty-session-automation-and-portability.html"
source_id: "tag:blogger.com,1999:blog-5931535581904587661.post-6143678466109076621"
author: "df"
labels:
  - "putty session portability"
  - "portable putty"
  - "keepass putty"
  - "putty"
  - "Technology"
  - "session automation"
  - "autoit putty"
---

<div dir="ltr" trbidi="on">
Hope you all have "Putty" as your favourite ssh client? For me too..&nbsp;&nbsp; But sometimes, I felt there are some issues when you are working with 100's of servers and multiple locations.&nbsp; This article will guide you to achieve<br />
<ul>
<li>Putty portability: by storing sessions in files rather than in windows Registry</li>
<li>Automate creation of Putty sessions: &nbsp;No more manual entries one by one</li>
<li>Consistent coloring of Putty sessions for team</li>
<li>Consistent naming conventions for Putty sessions</li>
<li>"Keepass" to putty integration: Password management and automated login</li>
<li>Use "SuperPutty" to allow multiple putty sessions in a single Tab</li>
</ul>
<h3>
Pre-requisite &nbsp;</h3>
<h4>
Full package available to download at end of this document</h4>
<ul>
<li>Basic knowledge of coding. Overall understanding of tools</li>
<li>Portable Putty: Ability to store sessions to file (<a href="http://jakub.kotrla.net/putty/">http://jakub.kotrla.net/putty/</a>)</li>
<li>Optional: AutoIT (<a href="http://www.autoitscript.com/site/autoit/">http://www.autoitscript.com/site/autoit/</a>) : For automation purpose in Windows PC's. (Alternatively *NIX env by writing a simple find-replace awk script)</li>
<li>Optional: SuperPutty (<a href="http://code.google.com/p/superputty/">http://code.google.com/p/superputty/</a>) to allow tab access</li>
<li>Optional: Keepass (<a href="http://keepass.info/">http://keepass.info/</a>) Password Management</li>
</ul>
<h3>
What we are going to do (in a nutshell)</h3>
<ul>
<li>Create putty sessions in batch from a configuration file</li>
<li>Configuration file format to contain IP address, hostname, Grouping etc..</li>
<li>Store sessions and Portable putty in consistent directory path. Share it to entire team if required to bring consistency across your team.</li>
<li>Link <em>Keepass</em> to use these saved sessions to allow manage password and login</li>
</ul>
<h3>
Step by Step guide</h3>
<ul>
<li>Download the package as given below of this document.</li>
<li>Unzip all the conents your local drive. (eg&nbsp; <em>C:\PuttyPortable\</em> )</li>
<li>Configure "<em>putty.conf</em>" as per your needs</li>
<li>Ensure you create "ses" and "hostkeys" directory as per "<em>putty.conf</em>"</li>
<li>Create color for sessions. This can be created based on the "Environment". Like Red color for "PROD" environment. Put then into a directory (eg. <em>C:\PuttyPortable\SessionConfig</em> )</li>
<li>Create Configuration file format to contain IP address, hostname, Grouping etc..&nbsp; (eg <em>C:\PuttyPortable\SessionConfig\ServerList.csv</em> )</li>
<li>Provide the Putty Session Template file. Provide correct port number if required (eg: <em>C:\PuttyPortable\SessionConfig\Template.Txt</em>)</li>
<li>I have created "<em>PuttySessionGenerator.au3</em>" automation script. Run it using "AutoIt3.exe"</li>
<li>Running This would create sessions in "ses" directory (eg: <em>C:\PuttyPortable\ses</em> )</li>
<li>Double click on your Putty (eg: <em>C:\PuttyPortable\putty.exe</em> ).</li>
<li>This will load all the new sessions automatically.</li>
<li>Link <em>Keepass</em> to use these saved sessions to allow manage password and lo-gins.&nbsp; Please use <a href="https://diaryfolio.com/2013/06/keepass-password-safe-bulk-actions.html" target="_blank">this guide</a></li>
</ul>
<h3>
Download Package</h3>
<a href="https://github.com/getkub/PuttyPortable" target="_blank">Download Code from GITHUB</a> (download by zip)<br />
<br />
<br />
This article is also listed under:<br />
<br />
<ul>
<li>Create Multiple Putty Sessions in one go</li>
<li>Putty Sessions as files rather than in registry</li>
<li>Bulk Create putty session connections</li>
</ul>
</div>
