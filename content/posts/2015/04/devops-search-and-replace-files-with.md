---
title: "DevOps : Search and replace files with JSON dataset and template Engine"
date: "2015-04-24T11:59:00Z"
updated: "2015-04-24T12:04:02.143Z"
legacy_url: "/2015/04/devops-search-and-replace-files-with.html"
source_id: "tag:blogger.com,1999:blog-5931535581904587661.post-1588868914196114124"
author: "df"
labels:
  - "python"
  - "regex"
  - "automation"
  - "devops"
  - "templates"
  - "JSON"
  - "pystache"
  - "config"
  - "mustache"
---

<div dir="ltr" trbidi="on">
Today's code build &amp; continuous deployment models are highly diverse thus leading to handwritten and complicated perl/awk/sed scripts. DevOps should come out of age old hand-crafted find and replace scripts with much modern template engines.<br />
<div class="separator">
<a href="/assets/images/original/2015/04/devops-search-and-replace-files-with/mustache.png" imageanchor="1"><img border="0" src="/assets/images/original/2015/04/devops-search-and-replace-files-with/mustache.png" height="114" width="320" /></a></div>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Of course template engines are available in wide variety. All enterprise configuration management (chef, puppet, ansible ) software are equipped with their own flavour of template engines and playbooks. &nbsp;This article however concentrate on <a href="https://mustache.github.io/" target="_blank">"Mustache" template </a>&nbsp;which is logicless template system and work on any text based data (Web pages, scripts, dataset, config files etc..)<br />
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; The example below focusses on replacing dynamic text using a JSON dataset. Let's define terminologies<br />
<ul>
<li><b>Source</b> : &nbsp; Template Parent Directory with all files/directories + &nbsp;dynamic variables in it</li>
<li><b>Dataset</b>: &nbsp; &nbsp;JSON based self defining dataset to replace the above source(s)</li>
<li><b>Params</b>: &nbsp; &nbsp;Extra parameters that are supplied (eg: Environment PROD, DEV etc..)</li>
</ul>
The key idea here is to replace all templates (<b><u>recursively</u></b>) within the "Parent Source Directory" and find and replace with dataset. In summary this is what I'm trying to achieve<br />
<ul>
<li>All template files in "<b><i>Source</i></b>" to have an extension of &nbsp;"<b><i>.mustache</i></b>"</li>
<li>Recursively scan whole of&nbsp;"<b><i>Source</i></b>"&nbsp;directory and children and identify &nbsp;.<i>mustache</i> files</li>
<li>Feed these files into <i>mustache</i> renderer</li>
<li>Rending information supplied using "<b><i>Dataset</i></b>"</li>
<li>Filter out required elements of "<b><i>Dataset</i></b>" using input "<b><i>Params</i></b>"</li>
<li>Copy directory structure and files into a temporary location with <i><b>filled</b></i> values</li>
</ul>
<br />


<br />
<br /></div>
