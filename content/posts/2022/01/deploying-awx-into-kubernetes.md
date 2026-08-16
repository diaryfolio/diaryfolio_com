---
title: "Deploying awx into kubernetes"
date: "2022-01-08T20:26:00.006Z"
updated: "2022-01-08T21:23:05.988Z"
legacy_url: "/2022/01/deploying-awx-into-kubernetes.html"
source_id: "tag:blogger.com,1999:blog-5931535581904587661.post-4490383588069464734"
author: "df"
labels:
  - "kubernetes"
  - "awx"
  - "automation"
  - "ansible"
---

<p>&nbsp;</p><h1>Deploying awx into kubernetes</h1><h2>Intro</h2><p>AWX provides a web-based user interface, REST API, and task engine built on top of Ansible. This article will summarise steps of installing AWX into Kubernetes&nbsp;using Operator</p><h2>Pre-Reqs</h2><p></p><ul><li>Familiarity with Kubernetes (k8s)</li><li>Bit powerful node machine of 4vCPU &amp; 8GB RAM</li><li>AWX is exposed on port 9080, so enable firewall accordingly (As default port 80 will have collision mostly in a Kubernetes environment)</li></ul><p></p><p></p><h2>Build Operator from code (Optional Step)</h2><div>Unfortunately at the time of writing, the official repository doesn't give a operator yaml directly, but suggests to build from code. But we use a pre-built operator yaml and hence below step of creating from source-code is optional</div><div><pre><code>apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  creationTimestamp: null
  labels:
    io.kompose.service: n8n-claim0
  name: n8n-claim0
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 2Gi
status: {}</code></pre></div><div><h2>Package components</h2></div><div>The deployment is split into following</div><div><ul><li><b>awx-operator.yaml&nbsp;</b>&nbsp;- Pre-built operator file</li><li><b>awx-pvc0.yaml&nbsp;</b>&nbsp;- PersistentVolumeClaim To mount directory awx</li><li><b>awx-deployment.yaml&nbsp;</b>&nbsp;- Actual deployment definitions</li><li><b>awx-svc.yaml&nbsp;</b>&nbsp;- Service To expose awx for UI access</li></ul><div><h3>awx-operator.yaml</h3><pre><code>kubectl create ns awx
</code></pre><pre><code>kubectl apply -f https://raw.githubusercontent.com/getkub/k8s_kubernetes/main/modules/awx/built_operator/awx-operator.yml
</code></pre></div></div><h3>awx-pvc0.yaml</h3><pre><code> apiVersion: v1
 kind: PersistentVolumeClaim
 metadata:
   name: static-data-pvc
 spec:
   accessModes:
     - ReadWriteOnce
   storageClassName: local-path
   resources:
     requests:
       storage: 2Gi</code></pre><h3>awx-deployment.yaml</h3><pre><code class="yaml">apiVersion: awx.ansible.com/v1beta1
kind: AWX
metadata:
  name: awx
spec:
  service_type: LoadBalancer
  loadbalancer_port: 9080
  projects_persistence: true
  projects_storage_access_mode: ReadWriteOnce
  web_extra_volume_mounts: |
    - name: static-data
      mountPath: /var/lib/awx/public
  extra_volumes: |
    - name: static-data
      persistentVolumeClaim:
        claimName: static-data-pvc
</code></pre><h3>awx-svc.yaml</h3><pre><code class="yaml">apiVersion: v1
kind: Service
metadata:
  name: awx-svc1
spec:
  ports:
  - port: 5432
    targetPort: 5432
    protocol: TCP
    name: awx-port
  selector:
    app: awx
  type: LoadBalancer
---</code></pre><div><h3>Apply in following order</h3><div><pre><code class="shell">kubectl create ns awx # Might be already created
kubectl -n awx apply -f &lt;operator&gt; # Might be already done<br />kubectl -n awx apply -f awx-pvc0.yaml<br />kubectl -n awx apply -f awx-deployment.yaml<br />kubectl -n awx apply -f awx-svc.yaml
</code></pre></div></div><div><pre><code class="shell">kubectl -n awx get all # To see all components</code></pre></div><div><pre><code class="shell">curl http://&lt;cluster_ip&gt;:9080
</code></pre><pre><br /></pre><pre><br /></pre></div><div><code class="shell"><br /></code></div><div class="separator"><a href="https://blogger.googleusercontent.com/img/a/AVvXsEj2ZhLGNCj6O4qwnBzwyCQVqVbB2uOm0cRjYO2Qt8PFppL-iML6xd_Zo7l4NwcrPBfr00GMntW_FSaf4wr-NXgxDiF1Lx4ynEONWljGNIR2WcS5TlcMuMwsUdIqNA-1cdLUAzRsT7u5pq_4d3_qUMzLVp4F40ZVf8sbPqHDgTvZpdCAaFuotxYGMKwJ=s521"><img border="0" data-original-height="302" data-original-width="521" height="185" src="https://blogger.googleusercontent.com/img/a/AVvXsEj2ZhLGNCj6O4qwnBzwyCQVqVbB2uOm0cRjYO2Qt8PFppL-iML6xd_Zo7l4NwcrPBfr00GMntW_FSaf4wr-NXgxDiF1Lx4ynEONWljGNIR2WcS5TlcMuMwsUdIqNA-1cdLUAzRsT7u5pq_4d3_qUMzLVp4F40ZVf8sbPqHDgTvZpdCAaFuotxYGMKwJ=s320" width="320" /></a></div><br /><div><br /></div>
