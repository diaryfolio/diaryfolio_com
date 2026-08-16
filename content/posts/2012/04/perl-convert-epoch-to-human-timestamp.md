---
title: "Perl Convert Epoch to Human timestamp YYYY-MM-DD HH:MM:SS"
date: "2012-04-04T09:40:00Z"
updated: "2014-06-22T17:25:40.526Z"
legacy_url: "/2012/04/perl-convert-epoch-to-human-timestamp.html"
source_id: "tag:blogger.com,1999:blog-5931535581904587661.post-3809703558904062553"
author: "df"
labels:
  - "Technology"
  - "human time"
  - "format"
  - "db2 time"
  - "epoch"
  - "timeformat"
  - "time conversion"
---

Ready made module in Perl to convert epoch time to DB2 or Human timestamp formats  (YYYY-MM-DD HH:MM:SS)<br/><br/>Write a function convertEpochToHumanTimestamp and call this from the required sub.<br/><blockquote>    # Function    : convertEpochToHumanTimestamp<br/># Description : Convert Epoch into a formatted time suitable for insertion into a Human database timestamp<br/>#               column. The output format is "YYYY-MM-DD HH:MM:SS"<br/><br/>my $inputEpoch = shift;<br/><br/>my ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = gmtime($inputEpoch);<br/>$mon++;<br/>$year = $year + 1900;<br/>my $humanTime = sprintf ("%04d-%02d-%02d %02d:%02d:%02d", $year, $mon, $mday, $hour, $min, $sec);<br/><br/>return ($humanTime);</blockquote>
