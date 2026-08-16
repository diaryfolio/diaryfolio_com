---
title: "Find process listening on a port"
date: "2012-04-20T14:41:00Z"
updated: "2014-06-22T17:25:40.534Z"
legacy_url: "/2012/04/find-process-listening-on-port.html"
source_id: "tag:blogger.com,1999:blog-5931535581904587661.post-9009998062585086391"
author: "df"
labels:
  - "listening process"
  - "aix"
  - "rmsock"
  - "Technology"
  - "tcpip"
  - "protocol control block"
  - "windows"
  - "port listen"
  - "netstat"
  - "pcb"
---

How to Find process listening on a port<br/><br/>I recently had an issue while implementing my web-server as the default port was used by something else.<br/>I used below commands in AIX to find more details of that process<br/><br/>1. Use netstat command to find the protocol control block or PCB which is a protocol layer for UDP or TCP sockets<br/><br/>eg.  netstat -Aan | grep &lt;port_number&gt;<br/>netstat -Aan | grep 30501<br/><br/>output will be something like<br/><blockquote>$ netstat -Aan | grep 30501<br/>f1000e0001363bb8 tcp4     0     0  *.30501     *.*     LISTEN</blockquote><br/>2. As "root" user, run rmsock command. Don't worry it won't remove anything as specified in the <a href="http://publib.boulder.ibm.com/infocenter/pseries/v5r3/index.jsp?topic=/com.ibm.aix.cmds/doc/aixcmds4/rmsock.htm">documentation</a>.<br/><br/>usage: rmsock Address TypeofAddress<br/><br/>eg.<br/><blockquote>rmsock f1000e0001363bb8 tcpcb<br/>output: The socket f1000e0001363bb8 is being held by proccess 15854120 (perl).</blockquote><br/>You can further diagnose the process using "ps -ef | grep &lt;process_id&gt;" and see the real process.<br/><br/>A good documentation can be found in<a href="http://www-01.ibm.com/support/docview.wss?uid=swg21264632"> IBM site</a> which caters for Windows as well.
