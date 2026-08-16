---
title: "Arithmetic/Math calculations using shell script &amp; Perl"
date: "2013-11-18T10:29:00Z"
updated: "2014-11-20T23:58:11.424Z"
legacy_url: "/2013/11/arithmeticmath-calculations-using-shell.html"
source_id: "tag:blogger.com,1999:blog-5931535581904587661.post-1587742379260394711"
author: "df"
labels:
  - "Technology"
---

<div dir="ltr" trbidi="on">
Unix Shell scripts are perfect when it comes to simple automation tasks. But the in-built calculations are quite poor compared to rest of its functionality. The main issues I've faced using out-of-box shell script functions like expr, bc, echo are<br />
<ul><br />
<li>Unable to calculate decimal places correctly</li>
<br />
<li>Error handling very poor (even divide by 0) and goes out of control.</li>
<br />
<li>Hard to control precision</li>
<br />
<li>Escape characters and regex increases complexity with formula</li>
</ul>
<br />
Object Oriented programs like Java/Python/.NET are excellent for arithmetic calculations. But this involves another level of coding and program installation. The trick I used is to use PERL which is built in almost all *nix distributions. Some of the advantages of using PERL within shell script are<br />
<ul><br />
<li>Easy to embed Perl commands into shell scripts</li>
<br />
<li>Most of *nix distro have PERL inbuilt</li>
<br />
<li>Reduced regex or escape character usage</li>
<br />
<li>Can put formulae into config file and can loop them into the shell script</li>
<br />
<li>precision, error handling are much better</li>
</ul>
<h3>
How to do math calculations in shell scripts</h3>
<ul><br />
<li>Write your shell script and put a function to do the real formula calculation</li>
<br />
<li>Use perl command line (-e) within shell script</li>
</ul>
<br />
<pre>perl -le 'printf "%.0f", eval"@ARGV"' "($VAL2-$VAL1)"</pre>
<br />
The above calculation will subtrace $VAL1 from $VAL2 and print with no decimal places (0f). The precision can be easily manipulated by changing the printf</div>
