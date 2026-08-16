---
title: "VMware to Virtualbox Migration"
date: "2016-03-06T17:50:00.001Z"
updated: "2022-01-01T10:34:29.981Z"
legacy_url: "/2016/03/vmware-to-virtualbox-migration.html"
source_id: "tag:blogger.com,1999:blog-5931535581904587661.post-51654125337692517"
author: "df"
labels:
  - "virtualbox"
  - "vmware"
  - "iaas"
---

<div dir="ltr" trbidi="on">
<a href="/assets/images/original/2016/03/vmware-to-virtualbox-migration/Virtualbox_logo.png" imageanchor="1"><img border="0" height="200" src="/assets/images/original/2016/03/vmware-to-virtualbox-migration/Virtualbox_logo.png" width="200" /></a>After updating my Fedora Kernel , VMware Workstation 12 stopped working. This moment I thought to switch back to Virtualbox as it has support for latest Kernels. There are pretty some good documentation on how to migrate from VMware to Virutalbox format<br />
<br />
<br />
You can find a good document on <a href="http://www.howtogeek.com/125640/how-to-convert-virtual-machines-between-virtualbox-and-vmware/" target="_blank">Migration Here</a>&nbsp;. In Summary the steps are<br />
<br />
<ul>
<li>Power off your guest which you are migrating</li>
<li>Open command promt as an Adminstrator and Navigate to &nbsp;&nbsp;<span><i><span>C:\Program Files (x86)\VMware\VMware Player\OVFTool</span></i></span></li>
<li><span>Run &nbsp;</span><span><span><i><b>ovftool &lt;source.vmx&gt; &lt;output.ovf&gt;</b></i></span></span></li>
</ul>
<div>
<span>eg&nbsp;</span></div>
<div>
<pre><span>ovftool "C:\Users\diaryfolio\Virtual Machines\Windows 7 x64\Windows 7 x64.vmx" C:\Users\diaryfolio\Win7Export.ovf</span></pre>
</div>
<ul>
<li>This would take about 15mins . So please be patient</li>
<li>Once complete Import into your Virtualbox using "Import Appliance"</li>
</ul>
<h3>
Errors that might occur</h3>
<div>
<ul>
<li>Error: "Failed to open disk” - This normally happens when the Guest VM is not properly shutdown or stopped</li>
<li>Error while importing to Virtualbox&nbsp;</li>
</ul>
<pre>Failed to import applianceHost resource of type "Other Storage Device (20)" is supported with SATA AHCI controllers only,
line 47. Result Code: VBOX_E_FILE_ERROR (0x80BB0004)
Component: Appliance Interface: Appliance {xxxxxxx-4add-4474-5bc3-xxxxxxxx}
</pre>
<div>
The quickest solution is to open it with any text/xml editor, and</div>
<div>
1. replace word “ElementName” with word “Caption” in the whole file</div>
<div>
2. replace “vmware.sata.ahci” with “AHCI”</div>
<div>
3. Then &nbsp;change SHA accordingly</div>
<pre><div>
[root@diaryfolio Win10 x64]# sha1sum "Win10 x64.ovf"</div>
0baac9938935a10b254e8cc18fc47fa3242168bb &nbsp;Win10 x64.ovf</pre>
</div>
</div>
