---
title: "Firefox - Remove slow and wave effect from high resolution monitors"
date: "2013-07-22T08:56:00Z"
updated: "2014-11-21T20:28:41.414Z"
legacy_url: "/2013/07/firefox-remove-slow-and-wave-effect.html"
source_id: "tag:blogger.com,1999:blog-5931535581904587661.post-4089706551179779203"
author: "df"
labels:
  - "firefox wavy"
  - "firefox hardware acceleration"
  - "Technology"
  - "Firefox slow"
  - "disable firefox hardware"
  - "firefox slow in external monitor"
---

<div dir="ltr" trbidi="on">
I am using laptop (with no special graphics card, but only inbuilt) and extending it to external monitor. The external monitor is high contrast and supports upto 1920 x 1080 (full HD) resolution. When Mozilla Firefox is opened in this high definition Monitor, it becomes very slow and wavy.&nbsp; The dragging effect is too much and discourages from using Firefox !!<br />
<br />
A solution to this is to "Disable Hardware Acceleration" within Firefox settings. To do this<br />
<ul><br />
<li>Firefox -&gt; Tools -&gt; Options -&gt; Advanced -&gt; General</li>
<br />
<li>Remove the "tick"&nbsp; from (Uncheck) "Use Hardware Acceleration when available"</li>
</ul>
<br />
<a href="http://incsi.org/dp/install/wordpress/wp-content/uploads/firefox_hardware_acceleration.jpg"><img alt="firefox_hardware_acceleration" class="alignnone size-medium wp-image-550" src="http://incsi.org/dp/install/wordpress/wp-content/uploads/firefox_hardware_acceleration-300x251.jpg" height="251" width="300" /></a><br />
<br />
Firefox fix has been tested on Samsung SyncMaster BX2240,&nbsp; Syncmaster 2443 monitors<br />
<br />
<span><strong>&nbsp;Advanced Users</strong></span><br />
<br />
<strong>about:config&nbsp;&nbsp; -&gt; layers.acceleration.disabled&nbsp;</strong> -&gt; change value to "<strong>true</strong>"<br />
<br />
<br />
<br />
</div>
