---
title: "Kubernetes & n8n: Setup n8n using K8S (Part 2) with TLS/https"
date: "2022-01-03T12:08:00.004Z"
updated: "2022-01-03T12:10:40.845Z"
legacy_url: "/2022/01/kubernetes-n8n-setup-n8n-using-k8s-part.html"
source_id: "tag:blogger.com,1999:blog-5931535581904587661.post-3221414577820186633"
author: "df"
labels:
  - "cacerts"
  - "kubernetes"
  - "cyber"
  - "n8n"
---

<p>We have briefly discussed on automating various tasks using n8n and installation of n8n within Kubernetes in <a href="https://diaryfolio.com/2021/12/kubernetes-n8n-setup-n8n-using-k8s-part.html" target="_blank">Part1</a>. In this part, we mostly concentrate on how to enable TLS (for https) and terminate before it hits n8n</p><p></p><div class="separator"></div><p></p><h2>Pre-Reqs</h2><p></p><ul><li>Setting up of n8n in Kubernetes ; Read&nbsp;<a href="https://diaryfolio.com/2021/12/kubernetes-n8n-setup-n8n-using-k8s-part.html" target="_blank">Part1</a></li><li>Knowledge of TLS, certificates</li></ul><p></p><h2>Summary Steps</h2><div><ul><li>Ensure n8n is configured properly with by http</li><li>Implement Kubernetes Ingress with https</li><li>There are two options from here</li><ol><li>End to end TLS by redirecting proxy to n8n&nbsp;</li><li>TLS termination at proxy and private network to be non-secure</li></ol><li>We follow the second option as it is easier, thus creating Ingress and pointing to <i>n8n</i> service</li></ul></div><h2>Steps</h2><h3>Steps in&nbsp;<i>lab_server</i></h3><p></p><ul><li>Ensure Certificate is created and implemented as a secret in Kubernetes preferably in same namespace</li></ul><pre><code class="shell">kubectl -n n8n create secret tls tls-secret --key test.key --cert test.crt
</code>
<ul><li>Use the same tls-secret in the Ingress config</li></ul><pre><code class="yaml">apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: n8n-ingress
spec:
  tls:
    - hosts:
      - n8n.mydev.test
      secretName: tls-secret
  rules:
  - host: n8n.mydev.test
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: n8n
            port:
              number: 5678

---</code></pre><div class="separator"><a href="https://blogger.googleusercontent.com/img/a/AVvXsEhItQxpvrqepyUbfwh6Ehypfm8J_5SwgLQa0zk3BmDgZxypfSYsZ_vNumWj72eC1PVGHTwOnC1tcI4XhQiiu68Yrwb7RLRXtUynBRaXMxfWhQKHH07Wmppgf4SoqgLOMeLIw6NaR5wyR5TqFOtXXbNhzvL-ru8nZHFX5b9mEbgr2F43m1yYTeqp4laE=s1270" imageanchor="1"><img border="0" data-original-height="760" data-original-width="1270" height="191" src="https://blogger.googleusercontent.com/img/a/AVvXsEhItQxpvrqepyUbfwh6Ehypfm8J_5SwgLQa0zk3BmDgZxypfSYsZ_vNumWj72eC1PVGHTwOnC1tcI4XhQiiu68Yrwb7RLRXtUynBRaXMxfWhQKHH07Wmppgf4SoqgLOMeLIw6NaR5wyR5TqFOtXXbNhzvL-ru8nZHFX5b9mEbgr2F43m1yYTeqp4laE=s320" width="320" /></a></div><br /><div class="separator"><br /></div><br /><h3><br /></h3><div><br /></div><div class="separator"><br /></div></pre>
