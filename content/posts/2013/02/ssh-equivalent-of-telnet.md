---
title: "ssh equivalent of telnet"
date: "2013-02-15T12:51:00Z"
updated: "2014-06-22T17:25:41.575Z"
legacy_url: "/2013/02/ssh-equivalent-of-telnet.html"
source_id: "tag:blogger.com,1999:blog-5931535581904587661.post-3764019658120551997"
author: "df"
labels:
  - "ssh"
  - "Technology"
  - "ssh for telnet"
  - "telnet alternative"
  - "telnet"
---

We will look into a method to do ssh equivalent for telnet<br/><br/>You guys must be familiar with running SSH. Using Standardport it would be<br/><blockquote>ssh &lt;serverIP&gt;</blockquote><br/><br/>If you want to run ssh on a non-standard port it is<br/><blockquote>ssh -p &lt;portNumber&gt; &lt;serverIp&gt;     #eg    ssh -p 5443   10.112.12.13</blockquote><br/><br/>But recently many Admins started removing "telnet" from *NIX machines. Previously Telnet was used to check if the remote machine was listening to a port and the connectivity. We used telnet as below<br/><blockquote>telnet &lt;serverIP&gt; &lt;portNumber&gt;  #eg   telnet  10.112.12.13 5443</blockquote><br/>You could simulate telnet using ssh command line. Though SSH is a protocol and not a debug tool, we could do some tricks.The equivalent of above telnet would be<br/><blockquote>ssh -vv -p 5443  10.112.12.13</blockquote><br/><br/><code><br/>ssh -p &lt;portNumber&gt; &lt;serverIp&gt; <br/>telnet &lt;serverIP&gt; &lt;portNumber&gt;<br/>ssh -vv -p 5443  10.112.12.13<br/></code>
