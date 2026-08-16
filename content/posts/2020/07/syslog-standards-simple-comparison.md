---
title: "Syslog Standards: A simple Comparison between RFC3164 & RFC5424"
date: "2020-07-18T18:37:00.009Z"
updated: "2024-04-07T06:11:33.859Z"
legacy_url: "/2020/07/syslog-standards-simple-comparison.html"
source_id: "tag:blogger.com,1999:blog-5931535581904587661.post-3661013180628124374"
author: "Kk"
labels:
  - "data science"
  - "syslog"
  - "big data"
---

<h2>Syslog Standards: A simple Comparison between RFC3164 (old format) &amp; RFC5424 (new format)</h2>Though syslog standards have been for quite long time, lot of people still
doesn't understand the formats in detail. The original standard document is
quite lengthy to read and purpose of this article is to explain with examples<h3>Some of things you might need to understand</h3>
<div>
  <ul>
    <li>
      The RFC standards can be used in any syslog daemon (syslog-ng, rsyslog
      etc.)
    </li>
    <li>
      Always try to capture the data in these standards. Especially when you
      have log aggregation like Splunk or Elastic, these templates are built-in
      which makes your life simple.
    </li>
    <li>Syslog can work with both UDP &amp; TCP&nbsp;</li>
  </ul>
  <h3>Link to the documents</h3>
</div>
<div>
  <ul>
    <li>
      <span>the original BSD format (</span><a href="https://tools.ietf.org/html/rfc3164" target="_blank">RFC3164</a><span>)</span>
    </li>
    <li>
      <span>the “new” format (</span><a href="https://tools.ietf.org/html/rfc5424" target="_blank">RFC5424</a><span>)</span></li></ul><div>
  </div>
  <div>
    <h3>
      RFC3164 (the old format)
    </h3>
    <div>
      <br />
    </div>
    <div>
      RFC3164 originated from combining multiple implementations (Year 2001)
        and have slightly different variations. But the message format should
        like&nbsp;
    </div>
    <div>
      <br />
    </div>
    <div></div>
  </div>
<pre><code>&lt;35&gt;Oct 12 22:14:15 client_machine su: 'su root' failed for joe on /dev/pts/2</code></pre>
  <div>
    <br />
  </div>
  <div>
    <div>
        <ul>
          <li>
            <div>
                &lt;35&gt; is a priority number. From the below matrix, you can
                see it is Auth , Error
              </div>
          </li>
          <li>
            <div>
              &nbsp;<i>Oct 12 22:14:15</i> is commonly known as syslog
              timestamp. Sometimes it will be ISO-8601 format too
            </div>
          </li>
          <li>
            <div>
              client_machine is the sender of the message (%hostname% field in
              payload)
            </div>
          </li>
          <li><div>su: is a tag (mostly process name)</div></li>
          <li>
            <div>Rest is the <i>MSG</i> component</div></li></ul></div>
  </div>
  <div>
    <h3>RFC5424 (the new format)</h3>
  </div>
  <div>
    RFC5424 came towards end of 2009 and is a better standard and more
      precise timestamp. The message limit is also configurable in this standard
      thus able to accept more than 1K size messages.
  </div>
  <div>
    <br />
  </div>

<pre><code>&lt;35&gt;1 2013-10-11T22:14:15.003Z client_machine su - - - 'su root' failed for joe on /dev/pts/2</code></pre></div>

  <div>
    <br />
  </div>
  <div>
    Also RFC5424 supports Structured Message payload in the MSG component
      making it easier for parsing.
  </div>
  
  <div><br /></div><div>
  </div>
  <div>
    <h3>Priority Matrix of Facility-Severity&nbsp;</h3><h3><ul><li>Header column is 'Severity'</li><li>Row column is 'Facility'</li><li>Each cell value is called Priority</li></ul></h3><div class="separator"><a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiPg6pNqBlxXD-0f9suSa72tzKtbW_Q-y8FEuUWpF85nfkv24da4g4VLn_ufhLAAAiMeWjMp8N7kcMyYH4YSv_AulW24cXMQ4gz4HOcXOGq8lm7P4rIdgXGaAgOU-k6TijfBo_rhBtqFOcW/s1622/Screenshot+2020-07-18+at+20.05.05.png"><img border="0" data-original-height="1622" data-original-width="1548" height="625" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiPg6pNqBlxXD-0f9suSa72tzKtbW_Q-y8FEuUWpF85nfkv24da4g4VLn_ufhLAAAiMeWjMp8N7kcMyYH4YSv_AulW24cXMQ4gz4HOcXOGq8lm7P4rIdgXGaAgOU-k6TijfBo_rhBtqFOcW/w595-h625/Screenshot+2020-07-18+at+20.05.05.png" width="595" /></a></div><div><br /></div>
  </div>
  <div><br /></div>
