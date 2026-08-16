---
title: "Elastic Beats on pfSense : Installation and configuration"
date: "2020-07-15T19:55:00.033Z"
updated: "2022-01-05T14:21:59.281Z"
legacy_url: "/2020/07/elastic-beats-on-pfsense-installation.html"
source_id: "tag:blogger.com,1999:blog-5931535581904587661.post-3848823481222519700"
author: "Kk"
labels:
  - "pfsense"
  - "vagrant"
  - "elastic"
  - "beats"
  - "siem"
---


<h2>Summary</h2>
Though in many cases syslog is preferred to transport the pfSense logs to external system, Elastic beats provides quite a niche way to send the logs while modelling the data alongside. This makes it ready-made to send to ElasticSearch directly and get ready-made outcomes like SIEM, performance etc.<br />
<h2> Pre-reqs </h2>
<ul>
   <li>A build server (preferably Ubuntu or Fedora) with internet connectivity </li>
   <li>shell access to pfsense server </li>
   <li>Basic knowledge of Elastic Stack (filebeat.yml configurations etc) </li>
   <li>Ensure connectivity is allowed from pfsense machine to your Elastic Stack receiver  </li>
   </ul><h2>Setup Summary</h2><ul>
   <li>Connectivity tests </li>
   <li>Install dependencies in build server (vagrant, virtualbox, gmake, go etc) </li>
   <li>Download Elastic Beats source </li>
   <li>Make elastic Beats package for FreeBSD </li>
   <li>Copy binary packages to pfsense server </li>
   <li>Configure Beats to send to destination </li>
   <li>Configure ElasticSearch to view the data </li>
</ul>
<h2> Installation Steps </h2>
<h3> Connectivity tests </h3>
    <pre> <code class="shell">Logon to pfsense server via Shell <br /> ssh root@192.168.1.1
<div>Password for root@pf.localdomain:pfSense - Netgate Device ID: 1a6323512345bf9e165d2<br />*** Welcome to pfSense 2.4.5-RELEASE (amd64) on pf ***<br /> WAN (wan)       -&gt; re0        -&gt; v4: 192.168.1.3/24<br /> LAN (lan)       -&gt; re1        -&gt; v4: 192.168.2.1/24<br /> 0) Logout (SSH only)                  9) pfTop<br /> 1) Assign Interfaces                 10) Filter Logs<br /> 2) Set interface(s) IP address       11) Restart webConfigurator<br /> 3) Reset webConfigurator password    12) PHP shell + pfSense tools<br /> 4) Reset to factory defaults         13) Update from console<br /> 5) Reboot system                     14) Disable Secure Shell (sshd)<br /> 6) Halt system                       15) Restore recent configuration<br /> 7) Ping host                         16) Restart PHP-FPM<br /> 8) Shell<br />Enter an option: 8</div></code></pre><div>
   <h3>Test connectivity to your ElasticSearch from pfsense</h3> 
    <pre><code class="shell">[root@pf.localdomain]/root: ssh -v -p 9200 192.168.1.10  # This is elasticSearch Server <br />OpenSSH_7.5p1, OpenSSL 1.0.2u-freebsd  20 Dec 2019debug1: Reading configuration data /etc/ssh/ssh_configdebug1: Connecting to 192.168.1.10 [192.168.1.10] port 9200.debug1: Connection established. <br />Test Internet connectivity from build Server (just ping github.com) <br />[root@buildserver]/tmp: ping github.com<br />PING github.com (140.82.118.4): <br />56 data bytes64 bytes from 140.82.118.4: icmp_seq=0 ttl=57 time=19.443 ms<br />64 bytes from 140.82.118.4: icmp_seq=1 ttl=57 time=19.348</code>    </pre><h3> Install dependencies in build server</h3><ul><li>Ensure VirtualBox is installed. (or follow <a href="https://www.blogger.com/#">link</a>) </li><li>Ensure Vagrant is installed  </li></ul> 
  
    <pre><code class="shell">[root@buildserver]/tmp: mkdir /tmp/freebsd <br />[root@buildserver]/tmp: cd /tmp/freebsd/ <br />[root@buildserver]/tmp/freebsd: wget https://releases.hashicorp.com/vagrant/2.2.9/vagrant_2.2.9_x86_64.deb [root@buildserver]/tmp/freebsd: apt install ./vagrant_2.2.9_x86_64.deb   </code></pre><h3>Create Vagrant file for FreeBSD </h3><div><ul><li>Update the vagrant file</li></ul></div> 
    <pre> <code class="shell">[[root@buildserver]/tmp/freebsd: vi Vagrantfile <br /> # FreeBSD Vagrant <br /> Vagrant.configure("2") do |config| <br />   config.vm.box = "freebsd/FreeBSD-11.2-RELEASE" <br />   config.vm.guest = :freebsd <br />   config.ssh.shell = "sh" <br />   config.vm.network "private_network", type: "dhcp" <br />   config.vm.synced_folder ".", "/vagrant", id: "vagrant-root", disabled: true <br />   config.vm.box_version = "2018.06.22" <br /> end <br />Bring up the container and ssh to it <br />[root@buildserver]/tmp/freebsd: vagrant up<br />[root@buildserver]/tmp/freebsd: vagrant ssh <br />Now the FreeBSD container is ready. Just logon to container and switch to root within it and install the dependencies <br /> [root@freeBSDContainer]/tmp/: pkg install git gmake go bashUpdating pfSense-core repository catalogue...pfSense-core repository is up to date.Updating pfSense repository catalogue.....The following 13 package(s) will be affected (of 0 checked): <br /> exit the shell and relogin  <br /> Download Elastic Beats source <br /> [root@freeBSDContainer]/root: go get github.com/elastic/beats<br />package github.com/elastic/beats: build constraints exclude all Go files in /root/go/src/github.com/elastic/beats </code><br /></pre>        
        Please take of the location <i>/root/go/src/github.com/elastic/beats</i></div><div><h3>Make elastic Beats package for FreeBSD </h3>
    <pre><code class="shell">[root@freeBSDContainer]/tmp: cd /root/go/src/github.com/elastic/beats <br />[root@freeBSDContainer]/tmp: git checkout v7.8.0 <br />[root@freeBSDContainer]/root/go/src/github.com/elastic/beats/filebeat: gmake <br />[root@freeBSDContainer]/root/go/src/github.com/elastic/beats/filebeat: file filebeat <br />[root@freeBSDContainer]/root/go/src/github.com/elastic/beats/filebeat: ./filebeat version <br />[root@freeBSDContainer]/root/go/src/github.com/elastic/beats/metricbeat: ./metricbeat version <br /></code></pre><h3>             
        Copy binary packages to pfsense server </h3><ul><li>Using scp or other methods, copy the file to pfsense server. Ideally its good to keep everything under <i>/opt/beats/ </i></li><li> configure Beats to send to destination in the relevant *beat.yml (eg <i>filebeat.yml)</i></li><li>Ideally you shouldn't start filebeat as root, but since this is for test purposes, we will do so. Else you need to create user and setup it correctly with least privileges </li></ul>
    <pre><code class="shell">[[root@pf.localdomain]/root/go/src/github.com/elastic/beats/filebeat: vi filebeat.yml <br /># ============================== Filebeat Config START ============================== <br />filebeat.config.modules: <br />  path: ${path.config}/modules.d/*.yml <br />  reload.enabled: true <br />  reload.period: 120s <br /># ---------------------------- Elasticsearch Output ---------------------------- <br />output.elasticsearch: <br />  hosts: ["192.168.1.10:9200"] <br />  protocol: "http" <br />  #api_key: "id:api_key" <br />  username: "elastic" <br />  password: "whateverpassword" <br /># ============================== Filebeat Config END ============================== <br />Ensure the relevant modules in filebeat are enabled <br />[root@pf.localdomain]/root/go/src/github.com/elastic/beats/filebeat: mv modules.d/auditd.yml.disabled modules.d/auditd.yml <br />Start filebeat  <br />[root@pf.localdomain]/root/go/src/github.com/elastic/beats/filebeat: ./filebeat -e <br />
        </code>
    </pre><ul><li> 
    check for any errors. otherwise you will see data coming to ElasticSearch cluster in few minutes. </li><li>Configure ElasticSearch to view the data (this includes indices, index-patterns, index-templates)</li></ul></div><div>&nbsp; <br /><a href="https://www.blogger.com/#"><img border="0" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhz07yb72MOL0TMVTC_dsbHL0BdsUbvh9-QFVfLzXbkD1a6fkyX6OdIoj57Qt5Y9GQSzRuqCPkFGLxnaw_JpOezONiAqmKqhAxsSidhzv88p7YSBs33miZmNHp-I5h2tnAkVmtN8ZM_ARym/s320/elk.jpg" /></a> <br />
</div>
