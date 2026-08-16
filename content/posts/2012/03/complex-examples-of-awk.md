---
title: "Complex examples of AWK"
date: "2012-03-06T14:52:00Z"
updated: "2014-06-22T17:25:40.062Z"
legacy_url: "/2012/03/complex-examples-of-awk.html"
source_id: "tag:blogger.com,1999:blog-5931535581904587661.post-5877560407934226820"
author: "df"
labels:
  - "multiple field separators"
  - "awk"
  - "Technology"
  - "awk one liners"
---

AWK is very powerful and newer generations nawk and gawk do have better flexibility. They are widely used by fellow scripters due to its sheen power.<br/>Let's look into some complex examples of AWK variants.<br/>I would recommend using nawk format as its installed in most of the Unix systems (AIX, Linux, Ubuntu have nawk by default)<br/><br/>Syntax for one line awk commands<br/><br/>&nbsp;<br/><blockquote>awk:  awk -Fs                     '/search/ {action}' awkvar=$shellvar infile<br/>nawk: awk -Fs -v awkvar=$shellvar '/search/ {action}'                  infile<br/>gawk: awk -Fs -v awkvar=$shellvar '/search/ {action}'                  infile</blockquote><br/>&nbsp;<br/><br/>BEGIN { }, { } and end { }<br/><br/>An awk script can have three types of blocks.<br/>One of them must be there.<br/>a) The BEGIN{} block is processed before the file is checked.<br/>b) The {} block runs for every line of input<br/>c) The END{} block is processed after the final line of the input file.<br/><br/>&nbsp;<br/><blockquote>awk '<br/>BEGIN    { myvalue = 1000 }<br/>/debt/   { myvalue -= $2  }<br/>/want/   { myvalue += $4  }<br/>END      { print myvalue  }<br/>' inputFile</blockquote><br/>&nbsp;<br/><br/>String functions<br/><blockquote>sub(regexp,sub)     Substitute sub for regexp in $0<br/>sub(regexp,sub,var)     Substitute sub for regexp in var<br/>gsub(regexp,sub)     Globally substitute sub for regexp in $0<br/>gsub(regexp,sub,var)     Globally substitute sub for regexp in var<br/>split(var,arr)     Split var on white space into arr<br/>split(var,arr,sep)     Split var on white space into arr on sep as separator<br/>index(bigvar,smallvar)     Find index of smallvar in bigvar<br/>match(bigvar,expr)     Find index for regexp in bigvar<br/>length(var)     Number of characters in var<br/>substr(var,num)     Extract chars from posistion num to end<br/>substr(var,num1,num2)     Extract chars from num1 through num2<br/>sprintf(format,vars)     Format vars to a string</blockquote><br/>#Multiple Field separator in Awk. use [][]. Below example will split whenever it finds  "?&gt;" in the data<br/><br/>awk -F'[?][&gt;]' '{print $2}' /tmp/abc.out<br/><br/>Courtesy: http://www.well.ox.ac.uk/~johnb/comp/awk/awk.html
