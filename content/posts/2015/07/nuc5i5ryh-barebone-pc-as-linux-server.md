---
title: "NUC5i5RYH - Barebone PC as Linux Server"
date: "2015-07-18T12:17:00.004Z"
updated: "2015-07-31T14:33:49.352Z"
legacy_url: "/2015/07/nuc5i5ryh-barebone-pc-as-linux-server.html"
source_id: "tag:blogger.com,1999:blog-5931535581904587661.post-7414615297456026898"
author: "df"
labels:
  - "intel"
  - "nuc"
  - "centos"
  - "vmware"
---

<div dir="ltr" trbidi="on">
After thinking of &nbsp;installing VMWare ESXi on&nbsp;NUC5i5RYH barebone , I decided not to go ahead. This is because you need a separate system to manage (vSphere Client) to manage your lab which in my case was not helpful. I decided to go ahead and install CentOS 7 as my main OS(host) and install VMware workstation to support Windows Server (for ActiveDirectory) as guest.<br />
<br />
I faced few issues while installing CentOS into the i5 NUC. Mainly because the CentOS Kernel &amp; drivers are bit outdated compared to NUC. Just to document what I've done to fix them !!<br />
<h3>
<a href="/assets/images/original/2015/07/nuc5i5ryh-barebone-pc-as-linux-server/nuc.jpg" imageanchor="1"><img border="0" height="148" src="/assets/images/original/2015/07/nuc5i5ryh-barebone-pc-as-linux-server/nuc.jpg" width="200" /></a>
Preparation&nbsp;</h3>
<ul>
<li>Download Minimal CentOS7 from main site</li>
<li>Use "UNetbootin" to put the ISO into thumbdrive.&nbsp;</li>
<li>FAT32 formatting of your USB is best suited</li>
</ul>
<h3>
Installation</h3>
<ul>
<li>Attach bootable USB to your NUC and enter ensure your USB as primary boot.</li>
<li>Ensure you create a "root" user and password</li>
<li>Reboot and CentOS installation is straight forward.&nbsp;</li>
</ul>
<h3>
Network Issues</h3>
Your Wi-Fi won't be listed in your detected devices (ifconfig, iwlist etc are not installed)<br />
<h3>
NetworkManager to your rescue</h3>
<div>
NetworkManager Command Line (nmcli) is very powerful. <a href="https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/7/html/Networking_Guide/sec-Using_the_NetworkManager_Command_Line_Tool_nmcli.html" target="_blank">Full details here</a></div>
<pre><div>
sudo su - # All activities in root</div>
<div>
nmcli device show &nbsp; # Shows all devices available. Only your ethernet and loop back would show</div>
<div>
nmcli con show # Shows connections available. You won't be able to see anything initially</div>
</pre>
<div>
<h3>
Installing Relevant Driver.&nbsp;</h3>
(You need an extra laptop for this)<br />
<ul>
</ul>
</div>
<div>
I had CentOS 7 with Kernel 3.10.x . <a href="https://wireless.wiki.kernel.org/en/users/drivers/iwlwifi" target="_blank">NUC5i5RYH uses Wireless 7265</a> ,but the downloads are meant for Kernel 3.13+ onwards. So I had to download multiple drivers thus facing lot of hit &amp; miss. I can confirm, the driver that works is &nbsp;"<a href="https://wireless.wiki.kernel.org/_media/en/users/drivers/iwlwifi-7265-ucode-25.228.9.0.tgz" target="_blank">iwlwifi-7265-ucode-25.228.9.0.tgz</a>" though it's for a higher Kernel. Extract just the "iwlwifi-7265-9.ucode" file from the archive and copy it into usb drive and copy it to<u><i> /lib/firmware/</i></u> of your CentOS installation. &nbsp;(USB mounting <a href="http://askubuntu.com/questions/37767/how-to-access-a-usb-flash-drive-from-the-terminal-how-can-i-mount-a-flash-driv" target="_blank">tips at this link</a>). Now REBOOT your NUC</div>
<div>
<h3>
Verify if your Network is detected.&nbsp;</h3>
</div>
<pre><div>
sudo su - # All activities in root</div>
<div>
nmcli device show &nbsp; # Shows all devices available. Now it show a wireless device (eg wls2p0)
</div>
<div>
nmcli con show # Connections won't be still available</div>
</pre>
<div>
if no devices are shown, something went wrong. Need to debug by running "dmesg | tail -100" to see if there are any errors when OS rebooted.</div>
<div>
<h3>
Add your interface</h3>
</div>
<div>
Now try adding a new connection to your interface using networkmanager cli (wls2p0 is my ifname shown when I ran &nbsp;"nmcli device show") . More <a href="https://docs.fedoraproject.org/en-US/Fedora/20/html/Networking_Guide/sec-Connecting_to_a_Network_Using_nmcli.html" target="_blank">Details in this link</a></div>
<br />
<pre><div>
nmcli con add con-name wls2p0 ifname wls2p0 type wifi ssid MyInternetConnectionName ip4 192.168.100.101/24 gw4 192.168.100.1</div>
<div>
service NetworkManager restart# This should restart network</div>
</pre>
<div>
You should be now able to see <i>ifcfg-wls2p0</i> file in <i>/etc/sysconfig/network-scripts/ </i>&nbsp;location with above details and will get a MAC address automatically.</div>
<div>
<h3>
Adding wifi plugin to NetworkManager</h3>
<div>
Unfortunately "NetworkManager" itself doesn't contain wifi setup plugins. You need to download <a href="http://rpm.pbone.net/index.php3/stat/4/idpl/28992640/dir/centos_7/com/NetworkManager-wifi-1.0.0-14.git20150121.b4ea599c.el7.x86_64.rpm.html" target="_blank">"NetworkManager-wifi" rpm</a> offline package separately into your laptop. Copy this again using usb into your NUC. &nbsp; Install it using &nbsp;rpm -Uvh &lt;rpmfile&gt;&nbsp;</div>
</div>
<div>
Verify if the package is installed</div>
<pre><div>
rpm -qa | grep NetworkManager</div>
<div>
service NetworkManager restart</div>
<div>
service NetworkManager status</div>
</pre>
<div>
<h3>
Connect your Wifi</h3>
<div>
nmcli device wifi connect &lt;MyInternetConnectionName&gt; password &lt;myPassword&gt;</div>
</div>
<div>
<br /></div>
<div>
Verify by running&nbsp;</div>
<div>
<pre>curl -k https://www.google.com&nbsp;</pre>
</div>
<div>
Atlast, it should all work now !!</div>
<div>
<br /></div>
Now you could install GUI by<br />
<span>sudo yum groups install "GNOME Desktop"</span><br />
<div>
<span><br /></span></div>
<br />
<br /></div>
