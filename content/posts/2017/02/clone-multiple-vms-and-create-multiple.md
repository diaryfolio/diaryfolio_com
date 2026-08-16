---
title: "Clone multiple VM's and create multiple VM's using vagrant"
date: "2017-02-04T16:23:00.004Z"
updated: "2017-02-04T16:25:37.807Z"
legacy_url: "/2017/02/clone-multiple-vms-and-create-multiple.html"
source_id: "tag:blogger.com,1999:blog-5931535581904587661.post-2824146948681785547"
author: "df"
labels:
  - "virtual machine"
  - "virtualbox"
  - "devops"
  - "vm"
  - "vmware"
  - "vagrant"
---

<div dir="ltr" trbidi="on">
Vagrant is an excellent tool for automation and doing proof of concepts (POC's). In many of the POC's you might need cluster and vagrant can do the clustering in matter of minutes by cloning an existing VM and then making into multiple Virtual machines<br />
<br />
<div class="separator">
<a href="/assets/images/original/2017/02/clone-multiple-vms-and-create-multiple/VagrantVBAnsible_diaryfolio.png" imageanchor="1"><img border="0" height="105" src="/assets/images/original/2017/02/clone-multiple-vms-and-create-multiple/VagrantVBAnsible_diaryfolio.png" width="400" /></a></div>
<br />
Assumption<br />
<br />
<ul>
<li>You have basic idea of Linux &amp; vagrant</li>
<li>we are going to use centos/7 for vagrant guest</li>
<li>The host is Fedora25/Redhat/CentOs system. Can be easily done for ubuntu as well</li>
</ul>
<br />
Let's see the overall Summary of what we are doing to do<br />
<br />
<ul>
<li>create a working directory</li>
<li>download and install virtualbox, then vagrant</li>
<li>clean-up any unwanted boxes you have.</li>
<li>putting the config file and provisioning</li>
<li>Validating the nodes</li>
</ul>
<div>
<br /></div>
<h4>
Creating a working Directory</h4>
<div>
sudo su -</div>
<div>
mkdir /opt/vagrantOps</div>
<div>
cd /opt/vagrantOps</div>
<div>
<br /></div>
<h4>
Download and Install vbox, vagrant to your host (Fedora 25)</h4>
<div>
vi /etc/yum.repos.d/virtualbox.repo &nbsp;# with contents as per <a href="http://download.virtualbox.org/virtualbox/rpm/fedora/virtualbox.repo" target="_blank">Virtualbox recommendation</a></div>
<br />
<div>
dnf install VirtualBox-5.1 &nbsp; # This will install vbox &nbsp;from above repo</div>
<div>
<div>
dnf install vagrant &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;# Vagrant core</div>
<div>
dnf install -y vagrant vagrant-libvirt libvirt-devel &nbsp; # Addons to vagrant</div>
</div>
<div>
<br /></div>
<h4>
clean-up and purge (if you want to start from scratch)</h4>
<div>
vagrant box list &nbsp;# to check list of boxes available</div>
<div>
vagrant global-status # Will show all running and available VM's</div>
<div>
vagrant destroy -f ${id} &nbsp; # Note the id from above command and destroy them</div>
<div>
<br /></div>
<h4>
putting the config file and provision</h4>
<div>
vagrant init &nbsp; &nbsp; &nbsp; &nbsp;# Ensure you are in vagrantOps directory and will create&nbsp;Vagrantfile</div>
<div>
# Copy code from <a href="https://github.com/getkub/SplunkScriplets/blob/master/thirdparty/vagrant/multivms.vagrantfile" target="_blank">github repo</a>&nbsp; and paste it to&nbsp;Vagrantfile</div>
<div class="separator">
<a href="/assets/images/original/2017/02/clone-multiple-vms-and-create-multiple/vagrant.multipleVM.diaryfolio.jpg" imageanchor="1"><img border="0" height="345" src="/assets/images/original/2017/02/clone-multiple-vms-and-create-multiple/vagrant.multipleVM.diaryfolio.jpg" width="640" /></a></div>
<div>
# The config file will provision 4 VM nodes with sample node names</div>
<div>
<br /></div>
<h4>
Validating the nodes</h4>
<div>
<div>
vagrant global-status # Will show all running and available VM's</div>
</div>
<div>
vagrant ssh diaryfolio_vm1 &nbsp; # name of the VM1</div>
<div>
<div>
vagrant ssh diaryfolio_vm2 &nbsp; # name of the VM2</div>
</div>
<div>
<br /></div>
<div>
<br /></div>
<br />
<div>
<br /></div>
<br />
<div>
</div>
</div>
