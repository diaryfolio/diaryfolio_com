---
title: "Kubernetes & n8n: Setup n8n using K8S (Part 1)"
date: "2021-12-28T10:35:00.010Z"
updated: "2025-08-13T04:03:00.293Z"
legacy_url: "/2021/12/kubernetes-n8n-setup-n8n-using-k8s-part.html"
source_id: "tag:blogger.com,1999:blog-5931535581904587661.post-5446431904899517870"
author: "Kk"
labels:
  - "cloud"
  - "kubernetes"
  - "n8n"
  - "k8s"
  - "soar"
---

<h2>&nbsp;Intro</h2><p>Aim of this article is to Publish <a href="https://n8n.io/" target="_blank">n8n</a> workflow automation tool into a Kubernetes environment.&nbsp; n8n is quite flexible and can be used for IOT devices for your hobby projects to act as a SOAR tool at enterprise level.</p><h4>NOTE</h4><p>A new version "<a href="https://diaryfolio.com/2025/08/scaling-great-workflow-system-n8n-on.html">Scaling n8n on Kuberetes</a>" is written for HELM chart based installation</p><h2>Pre-Reqs</h2><p></p><ul><li>Familiarity with Kubernetes (k8s)</li></ul><p></p><p>
</p><h2>Package components</h2><div>The deployment is split into following</div><div><ul><li><b>n8n-pvc0.yaml&nbsp;</b>&nbsp;- PersistentVolumeClaim To mount directory for n8n database and configs</li><li><b>n8n-pvc1.yaml&nbsp;</b>&nbsp;- PersistentVolumeClaim To mount directory for&nbsp;n8n workflows</li><li><b>n8n-deployment.yaml&nbsp;</b>&nbsp;- Actual deployment definitions</li><li><b>n8n-svc.yaml&nbsp;</b>&nbsp;- Service To expose n8n for UI access</li></ul></div>
<h4>n8n-pvc0.yaml</h4><pre><code>apiVersion: v1
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
status: {}
</code></pre>
<h4>n8n-pvc1.yaml</h4><pre><code>apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  creationTimestamp: null
  labels:
    io.kompose.service: n8n-claim1
  name: n8n-claim1
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 500Mi
status: {}
</code></pre>
<h4>n8n-deployment.yaml</h4><pre><code class="yaml">apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    io.kompose.service: n8n
  name: n8n
spec:
  replicas: 1
  selector:
    matchLabels:
      io.kompose.service: n8n
  strategy:
    type: Recreate
  template:
    metadata:
      labels:
        io.kompose.service: n8n
    spec:
      containers:
        - args:
            - n8n
            - start
          env:
            - name: N8N_BASIC_AUTH_ACTIVE
              value: "true"
            - name: N8N_BASIC_AUTH_PASSWORD
              value: thehive
            - name: N8N_BASIC_AUTH_USER
              value: thehive
            - name: N8N_PROTOCOL
              value: "http"
            - name: N8N_PORT
              value: "5678"
          image: n8nio/n8n
          name: n8n
          ports:
            - containerPort: 5678
          resources: {}
          volumeMounts:
            - mountPath: /root/.n8n
              name: n8n-claim0
            - mountPath: /opt/workflows
              name: n8n-claim1
      restartPolicy: Always
      volumes:
        - name: n8n-claim0
          persistentVolumeClaim:
            claimName: n8n-claim0
        - name: n8n-claim1
          persistentVolumeClaim:
            claimName: n8n-claim1
status: {}

</code></pre>
<h4>n8n-svc.yaml</h4>
<pre><code class="yaml">
apiVersion: v1
kind: Service
metadata:
  labels:
    io.kompose.service: n8n
  name: n8n
spec:
  ports:
    - name: "5678"
      port: 5678
      targetPort: 5678
  selector:
    io.kompose.service: n8n
status:
  loadBalancer: {}
</code></pre><div><br /></div>
<div><div>Apply in following order</div><div>
<pre><code class="shell">
kubectl create ns n8n
kubectl -n n8n apply -f n8n-pvc0.yaml
kubectl -n n8n apply -f n8n-pvc1.yaml
kubectl -n n8n apply -f n8n-deployment.yaml
kubectl -n n8n apply -f n8n-svc.yaml
</code></pre>
  
<br /></div></div><div>After few minutes, you should be able to access n8n UI from the service IP or depending on how you have exposed the service. Or another trick is to use `minikube tunnel`, and use the same ClusterIP to access it</div><div><br /></div><div><pre><code class="shell">curl http://&lt;cluster_ip&gt;:5678
</code></pre></div><div><code class="shell"><br /></code></div><div><code class="shell"><a href="https://blogger.googleusercontent.com/img/a/AVvXsEipPBDNCIsbJ9IndK_9qdmKps1zLFX3TScdQ6mt4tV_bFZjLKm2xJwYJZR1xvOI3uawKZsBm2J7NZ-uW-sSSSp_R2C798YJsARZkFB85irJumGMoZ5jGlw--28330ldMGefBe_tgKQekFgDKCLS-DtMfNFxg8UC0nLJAi-NPpmi93pxTnRD6PNP9EWr=s1270"><img border="0" data-original-height="760" data-original-width="1270" height="239" src="https://blogger.googleusercontent.com/img/a/AVvXsEipPBDNCIsbJ9IndK_9qdmKps1zLFX3TScdQ6mt4tV_bFZjLKm2xJwYJZR1xvOI3uawKZsBm2J7NZ-uW-sSSSp_R2C798YJsARZkFB85irJumGMoZ5jGlw--28330ldMGefBe_tgKQekFgDKCLS-DtMfNFxg8UC0nLJAi-NPpmi93pxTnRD6PNP9EWr=w400-h239" width="400" /></a></code></div>
