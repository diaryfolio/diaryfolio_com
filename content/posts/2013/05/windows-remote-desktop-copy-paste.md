---
title: "Windows Remote Desktop copy-paste workaround"
date: "2013-05-01T13:29:00Z"
updated: "2015-04-07T07:35:57.386Z"
legacy_url: "/2013/05/windows-remote-desktop-copy-paste.html"
source_id: "tag:blogger.com,1999:blog-5931535581904587661.post-8088825731061443463"
author: "df"
labels:
  - "remote desktop copy paste not working"
  - "remote desktop"
  - "rdpclip"
  - "Technology"
  - "copy-paste issue"
---

<div dir="ltr" trbidi="on">
Hope many guys had issues with windows remote desktop and ability to copy-paste items from your local machine to remote desktop? This guide shows how to fix if&nbsp;windows remote desktop copy-paste NOT working<br />
<div class="separator">
<a href="/assets/images/original/2013/05/windows-remote-desktop-copy-paste/Network-Remote-Desktop.png" imageanchor="1"><img border="0" src="/assets/images/original/2013/05/windows-remote-desktop-copy-paste/Network-Remote-Desktop.png" height="200" width="200" /></a></div>
<br />
<h2>
Workaround</h2>
<pre><ul>
<li>Connect to the development box using remote desktop&nbsp;&nbsp;(or alternatively run&nbsp; mstsc from run option) eg. 11.12.21.33</li>
<li>Put in your credentials and login to the Windows Server</li>
</ul>
</pre>
<h3>
Verify if clip is disabled</h3>
<pre>######### Below<strong> steps in Windows Server</strong> ############</pre>
<br />
<!--Ads1--><br />
<pre>In Windows Server -&gt; Start -&gt; Run -&gt; cmd&nbsp;&nbsp; to initiate the command prompt</pre>
<br />
Type in ..<br />
<pre>reg query "HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server\Winstations\RDP-Tcp" /v fDisableClip</pre>
<br />
The output might show<br />
<br />
<pre>fDisableClip&nbsp;&nbsp;&nbsp; REG_DWORD&nbsp;&nbsp;&nbsp; 0x1
 This means the clip got disabled.</pre>
<h3>
To <span><strong>enable</strong></span> fDisableClip</h3>
<pre>######### Below are the Actions in&nbsp; Windows Server ############</pre>
<br />
<pre>Start -&gt; Run -&gt; cmd -&gt; regedit

Navigate to HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server\Winstations\RDP-Tcp

Mouse single click on RDP-Tcp , so that a Right hand menu will come up

Please double click on "fDisableClip" to edit the Dword value

Please change the value from 1 to 0

Log off from Windows Server and login back after 2 minutes</pre>
<br />
Should be fixed by now :)<br />
<h3>
Medium-Long term fix</h3>
If the clip functionality is getting expired often, please <strong>kill</strong> the <span>rdpclip.exe</span> from taskmanager within the Server and restart the process again by<br />
<span><br /></span>
<br />
<pre><span>run rdpclip.exe</span></pre>
<br />
There are some miscellaneous/complex cases, whereby certain services needs to be started, but google is your friend!!<br />
<br />
<br />
<br /></div>
