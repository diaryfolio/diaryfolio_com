---
title: "Playing with Tar and gz commands"
date: "2012-03-19T11:44:00Z"
updated: "2014-06-22T17:25:40.300Z"
legacy_url: "/2012/03/playing-with-tar-and-gz-commands.html"
source_id: "tag:blogger.com,1999:blog-5931535581904587661.post-7765968732206103379"
author: "df"
labels:
  - "tar"
  - "Technology"
  - "unix zip"
  - "gunzip"
  - "gzip"
  - "packaging"
---

I was amused by Unix utilities. They are very powerful, but they are tricky for use. Let me note down some of them as they come along.<br/><blockquote>#To tar up *.log in the current directory into a tarball called abc.tar.gz, issue this command:<br/>tar cfz abc.tar.gz *.log<br/><br/>#untar<br/>tar xvf something.tar<br/><br/>#To see a list of the files within a tarball, issue the following command: # Helpful as its without untarring the file<br/>tar -tzf blah.tar.gz<br/># gunzip -c $file | tar xf -     #AIX<br/># Series of files<br/>while read file; do<br/>gunzip -c $file | tar xf -<br/>done &lt; filelist<br/><br/>#If you only want certain directories from the tarball, do this:<br/>tar xvzf something.tar.gz */dir.you.want/*</blockquote><br/>&nbsp;
