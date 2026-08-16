---
title: "Listing Installed Modules in Perl"
date: "2018-02-15T16:06:00.004Z"
updated: "2022-01-01T10:26:31.974Z"
legacy_url: "/2018/02/listing-installed-modules-in-perl.html"
source_id: "tag:blogger.com,1999:blog-5931535581904587661.post-2434607593667952974"
author: "df"
labels:
  - "perl"
  - "programming"
  - "modules"
---



<div dir="ltr" trbidi="on">
perl (Swiss Army Knife of Programming) is quite efficient in data processing. Though though not enterprise class as python, perl has a substantial presence in many packages including<br />
<div>
</div>
<ul>
<li>- git downloads for Windows</li>
<li>- present in all Linux Enterprise installations</li>
<li>- PAR (Perl Archive Toolkit) acts like a JAR file to be packaged up</li>
</ul>
<div class="separator">
</div>

<div>
One of the main problems you hit is the non-availability of packages or modules within perl.</div>
<div>
For instaance take the example of CSV module in perl. This is a very useful module if you want to play around with manipulating CSV.<br />
<br />
If you need to do cross platform scripts, below script is an efficient way to check the packages that are available "locally" in that server or machine before you start configuring your complex code.&nbsp; This can be a life saver and thus you can include your packages alongside if you need.</div>
<pre><code class="perl">
#!/usr/bin/perl
# list all of the perl modules installed
use File::Find ;
for (@INC) { find(\&amp;modules,$_) ; }
sub modules
{
        if (-d &amp;&amp; /^[a-z]/) { $File::Find::prune = 1 ; return }
        return unless /\.pm$/ ;
        my $fullPath = "$File::Find::dir/$_";
        $fullPath =~ s!\.pm$!!;
        $fullPath =~ s#/(\w+)$#::$1# ;
        print "$fullPath \n";
}
</code></pre>
<div><br /></div>
<div>
Above code will check for all available packages. You can then do a check for particular module.</div>
<div>
Also this script can be made as a function.</div>
<div>
<br /></div>

<div class="separator">
<a href="/assets/images/original/2018/02/listing-installed-modules-in-perl/perl.png"><img border="0" data-original-height="200" data-original-width="200" height="400" src="/assets/images/original/2018/02/listing-installed-modules-in-perl/perl.png" width="400" /></a></div></div>
