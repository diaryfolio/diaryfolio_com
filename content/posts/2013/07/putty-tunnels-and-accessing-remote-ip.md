---
title: "Putty Tunnels and Accessing remote IP blocked via firewall"
date: "2013-07-26T09:54:00Z"
updated: "2014-06-22T17:25:41.773Z"
legacy_url: "/2013/07/putty-tunnels-and-accessing-remote-ip.html"
source_id: "tag:blogger.com,1999:blog-5931535581904587661.post-5886023786207245613"
author: "df"
labels:
  - "port forwarding"
  - "tunnelling"
  - "putty"
  - "Technology"
  - "putty tunnels"
  - "corporate firewall"
---

This article will show step by step instructions How to setup tunnelling in Putty . This is extremely useful if a port is not opened over firewall but you can hop to a server with access and from there you can hop to another and so on.. Essentially it forwards port if you have access to atleast one port.<br/><ul><br/>	<li>Create a new SSH session - and save it. And click on load to load the settings. Choose the server and port  where you have already got access and firewall works. (eg.  ServerA, Port: 22)</li><br/>	<li><a href="http://incsi.org/dp/install/wordpress/wp-content/uploads/Clipboard-Image.jpg"><img class="alignnone size-medium wp-image-585" alt="Putty Create Session" src="http://incsi.org/dp/install/wordpress/wp-content/uploads/Clipboard-Image-287x300.jpg" width="287" height="300" /></a></li><br/>	<li>Select Tunnels from the Left Menu, specify the Source Port and Destination: The tunnel is created between the REMOTE UNIX box and your local machine (localhost). So, the source port will be the port on the REMOTE UNIX box  to which you want to talk to at a specific port which you can't access (eg Port 37150). And the destination will be your localhost, which will act as the other end your tunnel session</li><br/>	<li><img class="alignnone" alt="" src="http://img401.imageshack.us/img401/9313/3pnl.jpg" width="425" height="447" /></li><br/>	<li>[ad#ad-3]</li><br/>	<li><img alt="" src="http://img6.imageshack.us/img6/4923/koai.jpg" width="387" height="403" /></li><br/>	<li>Click Save after selecting the"Session"</li><br/>	<li>Open the saved session for which you just created the Tunnel and login to it.  This is because tunnels are created only when you login successfully . (eg. Access ServerA via port 22)</li><br/>	<li> To test Connectivity: Open a command prompt and try TELNET connection on the port   "C:/&gt; telnet localhost 37150"   . If the tunnel is successfully created a telnet connection should establish. Exit out of it.</li><br/>	<li> Access the URL of your application (or dmgr console) by replacing the IP address of the server with ‘localhost’. From the above example:<br/><strong>http://serverA:37150/</strong> would become <strong>http://localhost:37150/</strong></li><br/></ul>
