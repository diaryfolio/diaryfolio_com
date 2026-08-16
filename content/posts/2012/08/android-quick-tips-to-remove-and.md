---
title: "Android quick tips to remove and install an APK"
date: "2012-08-06T05:52:00Z"
updated: "2014-06-22T17:25:41.048Z"
legacy_url: "/2012/08/android-quick-tips-to-remove-and.html"
source_id: "tag:blogger.com,1999:blog-5931535581904587661.post-7865375758020176215"
author: "df"
labels:
  - "Technology"
  - "unlocking"
  - "android"
  - "adb commands"
---

Pre-req<br/><ul><br/>	<li>Need to have ADB installed</li><br/></ul><br/>Our aim is to install an old version of Music.apk onto a custom version. So the steps are like...<br/><ol><br/>	<li><strong>adb devices</strong>     #(shows list of devices attached)</li><br/>	<li><strong>adb remount</strong>   #mounts the directory for writing.</li><br/>	<li><strong>adb shell pm list packages -f  </strong>   #Lists all apps (.apk's) you have installed on phone</li><br/>	<li><strong>adb shell rm /system/app/Music2.apk</strong>                #Removes the apk.</li><br/>	<li><strong>adb push C:/pgms/"Music.apk" /system/app</strong>    #Specify full directory</li><br/>	<li><strong>adb shell pm list packages -f</strong>         #Confirm Music.apk  installation</li><br/>	<li><strong>exit</strong></li><br/></ol><br/>&nbsp;<br/><br/>[ad#ad-3]
