---
title: "Substitute data with a variable using &quot;awk and sed&quot;"
date: "2012-03-06T17:22:00Z"
updated: "2014-06-22T17:25:40.102Z"
legacy_url: "/2012/03/substitute-data-with-variable-using-and.html"
source_id: "tag:blogger.com,1999:blog-5931535581904587661.post-5893042082501274647"
author: "df"
labels:
  - "Technology"
---

Have you ever tried out substituting particular string with a variable? I thought it was easy.. but it is  NOT !! There are plenty of examples showing subsituting a fixed string with another fixed String.<br/><blockquote><br/><pre> # substitute (find and replace) "foo" with "bar" on each line<br/> awk '{sub(/foo/,"bar");print}'           # replaces only 1st instance<br/> awk '{gsub(/foo/,"bar");print}'          # replaces ALL instances in a line</pre><br/></blockquote><br/>But I had an issue to substitute  "foo" with value of "$bar" .. This is not easy. I did a workaround of using "awk" and "sed"<br/><br/>The scenario in front of me is to list a directory with files and the hostname of the Server.<br/><blockquote>thisHost=`hostname`<br/>ls -lrt | tail +2 | awk '{ print "thishost|"$9}' | sed "s/thishost/$thisHost/"</blockquote><br/>&nbsp;<br/><br/>tail +2 will remove the headers<br/><br/>The trick is to print  literal "thishost" and replace "thishost" literal using the value within sed.
