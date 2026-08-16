---
title: "C# online coding - Run .NET code online"
date: "2012-08-13T16:41:00Z"
updated: "2014-11-21T20:37:14.633Z"
legacy_url: "/2012/08/c-online-coding-run-net-code-online.html"
source_id: "tag:blogger.com,1999:blog-5931535581904587661.post-5949242383991165262"
author: "df"
labels:
  - "csharp online"
  - "c# online"
  - "run .net online"
  - ".net runtime"
  - "Technology"
---

<div dir="ltr" trbidi="on">
How to run .net code online ? A good question and very useful if you really want an OO programming language for your everyday use.&nbsp; There are some cool web-hosted runtimes for .NET<br />
<pre>http://www.ideone.com 
http://www.codepad.org
http://www.coderun.com 
http://www.compilr.com</pre>
<br />
I use <span><strong>codepad</strong> </span>and <span><strong>ideone</strong> </span>as they are simple and it JUST works all time!!<br />
<br />
Please find a simple snippet i wrote<br />
<br />
<pre>// To ensure each tokens are of 3 characters in length (else put space) and 
concatenate into a single string</pre>
<br />
<pre>using System;
 using System.Collections.Generic;
 namespace ClassLibrary
 {
 class Class1
 {
 static void Main() {
 string s = "123".PadRight(3).Substring(0,3);
 string s2 = "".PadRight(3).Substring(0,3);
 string s3 = "45".PadRight(3).Substring(0,3);
 string s4 = "6789".PadRight(3).Substring(0,3);
 System.Text.StringBuilder sb = new System.Text.StringBuilder();
 sb.Append(s);
 sb.Append(s2);
 sb.Append(s3);
 sb.Append(s4);
Console.Write(sb.ToString());
 }
 }
}</pre>
<br />
<h3>
Link to test</h3>
<a href="http://ideone.com/Ey4pi">http://ideone.com/Ey4pi</a></div>
