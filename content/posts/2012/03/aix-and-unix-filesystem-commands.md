---
title: "AIX and Unix filesystem commands"
date: "2012-03-19T11:50:00Z"
updated: "2014-06-22T17:25:40.339Z"
legacy_url: "/2012/03/aix-and-unix-filesystem-commands.html"
source_id: "tag:blogger.com,1999:blog-5931535581904587661.post-5235264620045825744"
author: "df"
labels:
  - "same filesystem"
  - "xdev"
  - "largest files"
  - "Technology"
  - "filesystem"
---

Everyone who works in IT industry and with Unix systems should have suffered filesystem related issues. The most common one is the filesystem getting filled up.<br/><br/>The scenario is<br/>Filesystem is filled up<br/>Determine largest files<br/>Filesystem is using different mounts. So the files you see are not within the filesystem.<br/>But there is a trick to find the largest files within the same filesystem<br/><br/>&nbsp;<br/><blockquote># Shows the largest 20 files within the same filesystem<br/># xdev will make sure its within the filesystem<br/><br/>find . -xdev -ls | sort +6 -nr | head -20</blockquote><br/>&nbsp;<br/><br/>Some other helpful commands in AIX to see the filesystem volume groups and if all disk is used<br/><blockquote>lsvg -o  # displays all volume groups<br/>lsvg -l &lt;lvname&gt; # list  (including mounts)<br/>lsvg &lt;lvname&gt;  # show details like free space etc</blockquote>
