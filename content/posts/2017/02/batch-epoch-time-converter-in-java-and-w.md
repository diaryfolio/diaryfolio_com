---
title: "Batch Epoch time converter in java and shell wrapper"
date: "2017-02-05T15:48:00Z"
updated: "2017-02-05T15:53:00.721Z"
legacy_url: "/2017/02/batch-epoch-time-converter-in-java-and-w.html"
source_id: "tag:blogger.com,1999:blog-5931535581904587661.post-1835828297351772561"
author: "df"
labels:
  - "epoch"
  - "utc"
  - "batch convert"
  - "human time"
  - "timestamp"
---

<div dir="ltr" trbidi="on">
I had to create a sample script to convert epoch time to Human readable format. &nbsp;(both ways)<br />
<div class="separator">
<a href="/assets/images/original/2017/02/batch-epoch-time-converter-in-java-and-w/epochTime_diaryfolio.JPG" imageanchor="1"><img border="0" height="266" src="/assets/images/original/2017/02/batch-epoch-time-converter-in-java-and-w/epochTime_diaryfolio.JPG" width="400" /></a></div>
<br />
Also from Human readable time format to Epoch. &nbsp;Input is a file with "Epoch" or "Human Readable" &nbsp;format and the program will convert in the other format. This could be used for embedding into your application or for batch convert, please find my program in Java<br />
<br />
<br />
<div dir="ltr" trbidi="on">
<div class="gistLoad" data-id="2e3db45086a7736aabbe5ca4d271c693" id="gist-2e3db45086a7736aabbe5ca4d271c693">
....
<br />
<br />
Afterwards, you can put this java file into a shell script if you want to automate your linux scripts<br />
<br />
Usage: &lt;scriptname&gt; &lt;inputfiletimeformat&gt; &lt;input_file_name_full_path&gt;<br />
<br /></div>
<div class="gistLoad" data-id="4aa191895875289dcb85b4c10f2df16f" id="gist-4aa191895875289dcb85b4c10f2df16f">
....
</div>
</div>
</div>
