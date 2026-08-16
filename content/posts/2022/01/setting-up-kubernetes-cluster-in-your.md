---
title: "Setting up Kubernetes Cluster in your home lab"
date: "2022-01-02T11:53:00.007Z"
updated: "2022-01-02T11:57:36.581Z"
legacy_url: "/2022/01/setting-up-kubernetes-cluster-in-your.html"
source_id: "tag:blogger.com,1999:blog-5931535581904587661.post-3529203906608356189"
author: "df"
labels:
  - "kubernetes"
  - "k8s"
  - "minikube"
  - "k3s"
  - "home-lab"
---

<h2>Summary</h2><p>Kubernetes&nbsp;is the future of&nbsp;automating deployment, scaling, and management of containerised applications which makes development of projects easier and portable. Additionally setting up such an environment within your local lab environment makes it easy to deploy and test out softwares at unprecedented pace.</p><p>You might have already setup Kubernetes&nbsp;in your laptop and must have used <i>minikube</i> to do so. But what if you want to setup it in your remote home lab? For instance i've got various DELL server (<i>lab_server</i>) running in my home lab and don't want my laptop to bear the pain of Kubernetes, but outsource the workloads to my&nbsp;<i>lab_server</i>&nbsp;while administering from <i>laptop</i></p><p></p><div class="separator"><br /></div><i><a href="https://k3s.io/" target="_blank">k3s</a> </i>is a lightweight alternative and <a href="https://github.com/alexellis/k3sup" target="_blank">k3sup</a> will automate such an installation into your&nbsp;<i>lab_server</i>&nbsp;and pair your <i>laptop</i> with it<p></p><h2>Pre-Reqs</h2><p></p><ul><li>Understanding of Kubernetes</li><li>sudo permission on your home lab and connectivity from your laptop</li><li>https://github.com/alexellis/k3sup</li><li>Add <i>lab_server</i> to <i>/etc/hosts </i>file of your <i>laptop</i></li></ul><p></p><h2>Steps</h2><h3>Steps in <i>lab_server</i></h3><p></p><ul><li>Create a dedicated user (eg: <i>k3user</i>) in <i>lab_server </i>with sudo permission</li><li>Ensure&nbsp;<i>k3user </i>can sudo without password prompt by following below step</li></ul><pre><code class="shell">sudo su - 
echo "k3user  ALL=(ALL) NOPASSWD: ALL" &gt; /etc/sudoers.d/k3user
chmod 0440 /etc/sudoers.d/k3user
exit</code>
</pre><pre><code class="shell"><ul><li>Ensure <i>management port (eg 6443)&nbsp;</i>is opened in Iptables/firewall-d etc to your LAN</li></ul><pre><code class="shell">sudo su -
iptables -I INPUT -s 192.168.1.0/24 -p tcp --dport 6443  -j ACCEPT
iptables-save &gt;/etc/iptables/rules.v4
exit</code></pre></code></pre><h3>
Steps in&nbsp;<i>laptop</i></h3><ul><li>Connect to the&nbsp;<i>home_server</i>&nbsp;using&nbsp;<i>k3user</i>&nbsp;and setup ssh-keys for automated access</li></ul><div><pre><code class="shell"># Generate key-pair if NOT done already
ssh-keygen -b 2048 -t rsa

# The above by default stores in your home location (~/.ssh/id_rsa)
# Copy the public key to lab_server and enter password one-time
ssh-copy-id -i ~/.ssh/id_rsa.pub k3user@lab_server<br /></code></pre></div><ul><li>Ensure you can connect and sudo without password prompt</li></ul><div><pre><code class="shell"># ssh to lab_server and ensure no password prompts
ssh k3user@lab_server

# now sudo to root without password prompt
sudo su -</code></pre></div><ul><li>Now setup k3s from your laptop.&nbsp;</li></ul><div><pre><code class="shell">curl -sLS https://get.k3sup.dev | sh
sudo install k3sup /usr/local/bin/ #Sometimes not required in Mac
k3sup --help # Check All works</code></pre></div><ul><li>Ensure you navigate to a relevant location as the <i>kubeconfig</i> file will be stored there by default and then run install</li></ul><div><div><pre><code class="shell">cd ~/mydev/
k3sup install --host lab_server --user k3user
# Note down the directory where kubeconfig is stored</code></pre></div><ul></ul></div><ul><li>Check if you can connect to lab_server and get kubectl info</li></ul><div><pre><code class="shell">export KUBECONFIG=`pwd`/kubeconfig
kubectl get node
kubectl get pods -A</code></pre></div><ul><li>All set to go now !!</li></ul><div><br /></div><div class="separator"><a href="https://blogger.googleusercontent.com/img/a/AVvXsEi6-F2NJDwQyUK2mfJSHmDKqmZrJUrZs7rlVAF5okqveEVrtFQKveFzsltRY8uEz0Wbv1hIZWT3jcg08ee6T-SwMghqnt2-04Y3SMrDuNTKo1rhbUH2ub6qAXsV8eis5k6RLQLljrhAN5-MJcR4CXS2L-zpeKMbFrwYuK2o58uxiqW-9dorSWVCikRF=s800" imageanchor="1"><img border="0" data-original-height="800" data-original-width="800" height="320" src="https://blogger.googleusercontent.com/img/a/AVvXsEi6-F2NJDwQyUK2mfJSHmDKqmZrJUrZs7rlVAF5okqveEVrtFQKveFzsltRY8uEz0Wbv1hIZWT3jcg08ee6T-SwMghqnt2-04Y3SMrDuNTKo1rhbUH2ub6qAXsV8eis5k6RLQLljrhAN5-MJcR4CXS2L-zpeKMbFrwYuK2o58uxiqW-9dorSWVCikRF=s320" width="320" /></a></div><br /><div><br /></div><br /><div><br /></div><div><br /></div><div><br /></div><div><br /></div><p></p>
