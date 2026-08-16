---
title: "Encrypted Filesystem - Virtual filesystem with folder, file and content encryption"
date: "2015-07-31T13:22:00.001Z"
updated: "2015-07-31T13:51:39.494Z"
legacy_url: "/2015/07/encrypted-filesystem-from-folder-with.html"
source_id: "tag:blogger.com,1999:blog-5931535581904587661.post-8330694519485110662"
author: "df"
labels:
  - "security"
  - "password"
  - "encryption"
  - "encfs"
  - "linux"
---

<div dir="ltr" trbidi="on">
Linux is wonderful when it comes to security aspects and data protection. My challenge was<br />
<br />
<ul>
<li>Laptop having personal details in files and folders</li>
<li>Have to encrypt these data so that if laptop is lost, the data shouldn't be replicated</li>
<li>Have to use "git" to backup the data normally and version it</li>
</ul>
<div>
<h3>
Solution for Linux</h3>
</div>
<div>
<h4>
<u>
Design your folder/directory structure</u></h4>
</div>
<div>
<a href="/assets/images/original/2015/07/encrypted-filesystem-from-folder-with/padlock.jpg" imageanchor="1"><img border="0" height="200" src="/assets/images/original/2015/07/encrypted-filesystem-from-folder-with/padlock.jpg" width="200" /></a><br />
<ul>
<li>Ensure that all your personal files are well structured</li>
<li>Ensure all files are put into a single directory/folder hierarchy &nbsp;(eg "/home/myuser/personal/")</li>
</ul>
<div>
<h4>
<u>
Setting up encfs</u></h4>
</div>
<div>
In Ubuntu, run&nbsp;</div>
</div>
<br />
<pre>sudo apt-get install encfs</pre>
<div>
<h4>
<u>Encrypted Directory and Mount location</u></h4>
</div>
<div>
<code>
encDir="/home/diaryfolio/Docs/encr" # Where encrypted files are stored</code></div>
mntDir="/home/diaryfolio/Docs/mydocs" # Mount created<br />
<div>
<div>
<br /></div>
<div>
# Create encrypted directory and mount directory</div>
<div>
<code>encfs $encDir $mntDir</code></div>
</div>
<div>
<br /></div>
<div>
# Press Enter which uses default encryption</div>
<div>
# Provide a strong password and REMEMBER it in future</div>
<div>
<br /></div>
<div>
# Copy content/files/directories to $mntDir once you mount it</div>
<div>
<br /></div>
<div>
# Unmount $mntDir afterwards</div>
<div>
<code>fusermount -u $mntDir</code></div>
<div>
<br /></div>
<div>
# You can now only see $encDir &nbsp;and encrypted files</div>
<div>
<br /></div>
<div>
# To remount and view files in plain format. It will ask you for your password</div>
<div>
<code>encfs $encDir $mntDir</code></div>
<div>
</div>
</div>
