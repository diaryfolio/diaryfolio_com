---
title: "Siteminder Custom Agent Installation"
date: "2012-10-02T14:27:00Z"
updated: "2014-11-21T00:10:20.534Z"
legacy_url: "/2012/10/siteminder-custom-agent-installation.html"
source_id: "tag:blogger.com,1999:blog-5931535581904587661.post-4616895123370575846"
author: "df"
labels:
  - "enterprise Single Sign-on"
  - "Technology"
  - "siteminder"
---

<div dir="ltr" trbidi="on">
I was trying to install single sign-on for an application. This has to be enabled using Siteminder Custom Agent and we wrote a test program to check the connectivity.<br />
<br />
This blog will note down the main hurdles and solutions if found.<br />
<h3>
<span>Issues Encountered</span></h3>
<ul><br />
<li><span>Following Parameters should be configured at Siteminder Policy Server end. This should be tied up in the Custom agent level as well.</span>- Siteminder Policy Server IP</li>
</ul>
<br />
<pre> - Policy Server Connection Minimum value
 - Policy Server Connection Maximum value
 - Policy Server Connection Step value
 - Policy Server Connection Timeout value
 - Policy Server Connection Accounting Port
 - Policy Server Connection Authentication Port
 - Policy Server Connection Authorization Port
 - An agreed unique Agent Name
 - Agent Secret agreed between agent and Policy Server
 - Agent IP (client/custom agent IP)
 - The resource page to protect</pre>
<ul><br />
<li><span>Error while initializing the STUB program.&nbsp;&nbsp; The error was mainly focussed on Linking the libraries. FATAL ERROR:</span></li>
</ul>
<br />
<pre>FATAL ERROR: Exception from System.loadLibrary(smjavaagentapi) java.lang.UnsatisfiedLinkError: smjavaagentapi (No such file or directory)
FATAL ERROR: Exception from AgentAPI.initialize() java.lang.UnsatisfiedLinkError: netegrity/siteminder/javaagent/AgentAPI.initialize()V</pre>
<br />
<pre>Exception in thread "main" java.lang.UnsatisfiedLinkError: netegrity/siteminder/javaagent/AgentAPI.javaagent_api_init(Lnetegrity/siteminder/javaagent/InitDef;)I
 at netegrity.siteminder.javaagent.AgentAPI.init(AgentAPI.java:xxx)</pre>
<br />
<h3>
<span>Solution</span></h3>
This is caused mainly due to <strong>incompatible</strong> versions of "<em><strong>java</strong></em>" with siteminder API's.<br />
We had JAVA5 as the main java version. I forced the <strong><em>LIBPATH</em> </strong>to <strong><span>64 bit Java6</span></strong> version and this worked !!<br />
<br />
</div>
