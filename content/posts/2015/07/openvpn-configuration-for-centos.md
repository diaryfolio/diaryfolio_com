---
title: "OpenVPN configuration for CentOS"
date: "2015-07-18T18:32:00.002Z"
updated: "2015-07-31T13:49:00.089Z"
legacy_url: "/2015/07/openvpn-configuration-for-centos.html"
source_id: "tag:blogger.com,1999:blog-5931535581904587661.post-7298117574652003029"
author: "df"
labels:
  - "pia"
  - "vpn"
  - "centos"
  - "openvpn"
  - "privateinternetaccess"
---

<div dir="ltr" trbidi="on">
<a href="/assets/images/original/2015/07/openvpn-configuration-for-centos/vpn.jpg" imageanchor="1"><img border="0" height="200" src="/assets/images/original/2015/07/openvpn-configuration-for-centos/vpn.jpg" width="200" /></a>This article is specifically for PrivateInternetAccess on CentOS. As you might see there are no written packages/support for CentOS. I've followed a very good <a href="http://www.gigahype.com/configure-openvpn-centos-privateinternetaccess/" target="_blank">article from this link</a> , but that was not enough as I had to tweak a lot afterwards.<br />
Just to write down the key points here<br />
<br />
<ul>
<li>Install OpenVPN using yum (enable <a href="http://fedoraproject.org/wiki/EPEL" target="_blank">EPEL</a> beforehand)</li>
</ul>
<div>
&nbsp;sudo yum install openvpn</div>
<div>
<br /></div>
<div>
Please follow all steps as per this article.&nbsp;</div>
<div>
Hope you have copied all VPN files in /etc/openvpn and the credentials to /root/.pia</div>
<div>
<br /></div>
<h4>
When you start, VPN it throws an error</h4>
<br />
<div>
[root@localhost openvpn]# systemctl start openvpn@server.service</div>
<div>
<div>
Job for openvpn@server.service failed. See 'systemctl status openvpn@server.service' and 'journalctl -xn' for details.</div>
</div>
<div>
<br /></div>
<div>
This is because you need to ensure the files/configurations you put in /etc/openvpn needs to be "<b><i>Set files with the openvpn_etc_t type</i></b>"</div>
<br />
<div>
<br /></div>
<h3>
How to set files with a specific type</h3>
<div>
<br /></div>
<div>
Please follow below instructions</div>
<div>
sudo su -&nbsp;</div>
<div>
cd /etc/openvpn/</div>
<div>
semanage fcontext -a -t openvpn_etc_t &nbsp;&lt;each_file&gt;</div>
<div>
/sbin/restorecon -v &nbsp;&lt;each_file&gt;</div>
<div>
<br /></div>
<div>
later you check status or start/stop vpn</div>
<div>
systemctl status openvpn@server.service</div>
<div>
systemctl start openvpn@server.service</div>
<div>
systemctl stop openvpn@server.service</div>
</div>
