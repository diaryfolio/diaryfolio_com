---
title: "Android Bios aka Recovery console"
date: "2012-08-28T14:31:00Z"
updated: "2014-06-22T17:25:41.150Z"
legacy_url: "/2012/08/android-bios-aka-recovery-console.html"
source_id: "tag:blogger.com,1999:blog-5931535581904587661.post-4392098272607079061"
author: "df"
labels:
  - "cwm console"
  - "Technology"
  - "unlocking"
  - "android"
  - "android bios"
  - "recovery android phones"
---

Hope you must be aware of Windows BIOS? A similar concept do exist in Android devices, but special thanks to Koush who exploited this and created a simple to use Recovery console with some powerful options. ClockwordMod (also known as CWM) has been used extensively by Android fellas to get control and manipulate Android devices.<br/><br/>Theory apart, let's deep dive into some of the ClockwordMod procedures<br/><h4>Pre-requisites.</h4><br/><ul><br/>	<li>Unzip /Archive Software. I prefer <a href="http://www.7-zip.org/download.html" target="_blank">7zip</a>.</li><br/>	<li>Either (<a href="http://developer.android.com/sdk/index.html" target="_blank">Android SDK</a>)  OR else (Install <a href="http://forum.xda-developers.com/showthread.php?t=1484405" target="_blank">ADB</a>+ Wrapper scripts)</li><br/>	<li>Device specific Clockwork Image (<a href="http://www.clockworkmod.com/rommanager/" target="_blank">List here</a>).</li><br/></ul><br/><h4>ClockworkMod Installation</h4><br/><ul><br/>	<li>Unzip the above ADB or Android SDK into a directory (eg   C:\myTestLocation\&lt;unzipHere&gt;\)</li><br/>	<li>Ensure your phone has sufficient charge to run in battery mode for sometime. Ensure your phone is ON.</li><br/>	<li>Connect the phone to your PC. Most of the cases, device specific (OEM) drivers will be installed.</li><br/>	<li>Now enable Debugging. (Settings &gt; Applications &gt; Development &gt; USB Debugging)</li><br/>	<li>Normally some extra drivers will be installed (if its the first time)</li><br/>	<li>Open a command window (Start -&gt; Run -&gt; cmd ) or (Windows Key + R). Change directory to where the ADB was unzipped. (i.e. C:\myTestLocation\&lt;unzipHere&gt;\ )</li><br/>	<li>Type "adb-windows.exe reboot bootloader"  into your cmd prompt.   The phone will reboot to a great Android man and stay there</li><br/>	<li>Now type "fastboot-windows.exe flash recovery recovery-clockwork-1.2.3-zte.img"</li><br/>	<li>It will say recovery sending... Okay, Recovery writing...</li><br/>	<li>Now type "fastboot-windows.exe reboot"</li><br/>	<li>Once your phone has started up type "adb-windows.exe reboot recovery" and you will be in Clockwork Mod Recovery</li><br/></ul>
