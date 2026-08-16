---
title: "Keepass Password Safe - Bulk Actions using field references"
date: "2013-06-24T11:22:00Z"
updated: "2014-11-21T20:23:12.586Z"
legacy_url: "/2013/06/keepass-password-safe-bulk-actions.html"
source_id: "tag:blogger.com,1999:blog-5931535581904587661.post-5264716290794772348"
author: "df"
labels:
  - "bulk password change"
  - "keepass batch mode"
  - "keepass"
  - "keepass bulk"
  - "Technology"
---

<div dir="ltr" trbidi="on">
Keepass password vault and the simplicity of the tool are essential if your day to day work. But I always encountered problem when it came to bulk actions; especially when passwords were the same for a set of servers (group)<br />
<h3>
Bulk Actions on Keepass</h3>
To do bulk actions (mass batch changes) , it is always advisable to have your list organized into groups. So that in future you can make it more granular. Below is a sample to reference a single master password for a group of NON-PROD Unix Servers<br />
<ul>
<li>Create a MASTER entry into the group.&nbsp; (eg&nbsp; MASTER_NON_PROD_UNIX)</li>
<li>Put your group password into this entry</li>
<li>Edit the individual entries which you want to reference this MASTER entry</li>
<li>Within the Edit Window -&gt; Remove any entries from "Password" and "Repeat" fields</li>
<li>Within the Edit Window -&gt; Tools -&gt; Insert Field Reference -&gt; "In password Field"&nbsp; <a href="http://incsi.org/dp/install/wordpress/wp-content/uploads/k1.png"><img alt="k1" class="alignnone size-medium wp-image-518" src="http://incsi.org/dp/install/wordpress/wp-content/uploads/k1-300x243.png" height="243" width="300" /></a></li>
<br />
<li>Select the MASTER entry from the list.</li>
<li>Identify source entry by "UUID"&nbsp;&nbsp; , Source field to reference "Password".&nbsp; <a href="http://incsi.org/dp/install/wordpress/wp-content/uploads/k2.png"><img alt="Keepass2" class="alignnone size-medium wp-image-517" src="http://incsi.org/dp/install/wordpress/wp-content/uploads/k2-300x60.png" height="60" width="300" /></a></li>
<br />
<li>Save the settings.</li>
<li>Next time, you just need to change the master entry and the rest of the group entries will follow the master.</li>
</ul>
</div>
