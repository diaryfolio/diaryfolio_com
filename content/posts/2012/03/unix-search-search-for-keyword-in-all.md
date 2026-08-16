---
title: "Unix Search - Search for a keyword in all the files"
date: "2012-03-19T11:38:00Z"
updated: "2014-06-22T17:25:40.291Z"
legacy_url: "/2012/03/unix-search-search-for-keyword-in-all.html"
source_id: "tag:blogger.com,1999:blog-5931535581904587661.post-7603969010200168601"
author: "df"
labels:
  - "Unix find"
  - "Deep search"
  - "Unix Search keyword"
  - "deep find"
  - "Technology"
---

I know everyone knows how to search for a file or directory in Unix.<br/><br/>Have you encountered a major issue and wanted to search for a keyword? Its like finding needle in a haystack. Believe me its very simple in Unix and *nix servers.  Let me call it as "Deep Search" !!<br/><br/>Please find the simple command<br/><blockquote># This will search all the *.log files for keyword "test"<br/># .  will mean all directories under the pwd. Change "." to "/" to search whole of the system. But remember to redirect errors<br/>find . -name "*.log" -exec grep -l "test" {} \;</blockquote>
