---
title: "Print next line after a pattern"
date: "2012-05-23T12:23:00Z"
updated: "2014-06-22T17:25:40.666Z"
legacy_url: "/2012/05/print-next-line-after-pattern.html"
source_id: "tag:blogger.com,1999:blog-5931535581904587661.post-1560668923783290049"
author: "df"
labels:
  - "print next line"
  - "one liners"
  - "awk"
  - "Technology"
---

Just had a requirement to print the current line with pattern and next line.<br/><br/>This seems to be pretty straight forward with AWK<br/><blockquote>awk '/YOUR_STRING/{c=1;{print}next}c--&gt;0'   &lt;yourFile&gt;</blockquote><br/>if you put c=2, it will print the next two lines<br/><br/>&nbsp;<br/><br/>Eg.  sampleData.txt containg..<br/><br/><em>EmployeeName</em><br/><em>ABC</em><br/><em>XYZ</em><br/><em>QPR</em><br/><em>LMN</em><br/><blockquote>awk '/EmployeeName/{c=1;{print}next}c--&gt;0'   sampleData.txt</blockquote><br/>will print..<br/><br/><em>EmployeeName</em><br/><em>ABC</em><br/><br/>if you don't want headers..<br/><blockquote>awk '/EmployeeName/{c=1;next}c--&gt;0'   sampleData.txt</blockquote><br/>&nbsp;
