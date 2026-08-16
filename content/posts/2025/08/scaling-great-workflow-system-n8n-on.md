---
title: "Scaling the Great Workflow System: n8n kubernetes helm chart"
date: "2025-08-13T03:52:00.006Z"
updated: "2025-08-26T23:00:13.684Z"
legacy_url: "/2025/08/scaling-great-workflow-system-n8n-on.html"
source_id: "tag:blogger.com,1999:blog-5931535581904587661.post-2222702042262127504"
author: "df"
labels:
  - "n8n"
  - "kubernetes"
  - "helm"
---

<p><strong>n8n</strong> is an extendable workflow automation tool that empowers teams to connect APIs, services, and data pipelines with ease. While it's a breeze to get started locally, deploying n8n on Kubernetes unlocks a new level of scalability, resilience, and automation — especially when using <strong>Helm</strong> to manage the lifecycle.</p>

<p>In this guide, we walk through deploying n8n to a Kubernetes cluster using a custom Helm-based setup, backed by official OCI charts and automation scripts that make the experience fast and production-ready.</p>

<h3>Project Structure</h3>
<pre><code>n8n/
├── Chart.yaml              # Helm chart metadata
├── values.yaml             # Configuration for n8n (DB, persistence, scaling)
├── templates/              # Kubernetes resource templates (Deployment, Service, PVC, Ingress)
│   ├── _helpers.tpl
│   ├── deployment.yaml
│   ├── ingress.yaml
│   ├── pvc.yaml
│   └── service.yaml
├── scripts/                # Shell scripts for operational tasks
│   ├── deploy.sh
│   ├── uninstall.sh
│   └── cleanup.sh
└── README.md               # Documentation and usage guide
</code></pre>

<h3>Code Location</h3><div>Github <a href="https://github.com/getkub/k8s_kubernetes/tree/main/isolated/n8n" target="_blank">Link</a></div><h3>Pre-requisites</h3>
<ul>
  <li>A working <strong>Kubernetes cluster</strong> (minikube, k3s, EKS, GKE, etc.)</li>
  <li><strong>Helm 3.8+</strong></li>
  <li><strong>kubectl</strong>, pointing to the desired cluster</li>
  <li>Optional: An external <strong>PostgreSQL</strong> or <strong>MySQL</strong> database</li>
</ul><br /><div><br /></div>

<h3>Deploying n8n</h3>
<p>Run the deployment script:</p>
<pre><code>./scripts/deploy.sh</code></pre>
<p>This will:</p>
<ul>
  <li>Create the namespace <code>n8n-system</code> if it doesn’t exist</li>
  <li>Deploy n8n from the official OCI Helm registry: <code>oci://8gears.container-registry.com/library/n8n</code></li>
</ul>

<h3>Verify Deployment</h3>
<p>Check the pods:</p>
<pre><code>kubectl get pods -n n8n-system</code></pre>
<p>Sample output:</p>
<pre><code>NAME                       READY   STATUS    RESTARTS   AGE
n8n-6c6fd9d6d4-8q9d8       1/1     Running   0          2m
</code></pre>

<h3>Access n8n</h3>
<p>If ingress is not configured, use port-forwarding:</p>
<pre><code>kubectl port-forward svc/n8n-stack-n8n-stack 5678:80 -n n8n-system &amp;</code></pre>
<p>Then open <a href="http://localhost:5678" target="_blank">http://localhost:5678</a> in your browser.</p>

<h3>Configuration</h3>
<p>Edit <code>values.yaml</code> to update key settings:</p>
<pre><code>config:
  database:
    type: postgresdb
    postgresdb:
      host: postgres.n8n-system.svc.cluster.local
      database: n8n
      user: n8n_user

secret:
  database:
    postgresdb:
      password: "your_postgres_password"

persistence:
  enabled: true
  size: 5Gi
</code></pre>
<ul>
  <li><code>config</code> holds non-sensitive values</li>
  <li><code>secret</code> contains secure credentials (used as Kubernetes Secrets)</li>
  <li><code>persistence</code> enables durable volume storage</li>
</ul>

<h3>Scaling with Queue Mode</h3>
<p>Enable queue mode and add Redis to scale horizontally:</p>
<pre><code>scaling:
  enabled: true
  worker:
    count: 2
  redis:
    host: "redis-host"
    password: "redis-password"
</code></pre>
<p>In queue mode:</p>
<ul>
  <li>The main pod handles the UI and triggers</li>
  <li>Worker pods run workflows in parallel</li>
  <li>Redis acts as the shared queue backend</li>
</ul>

<h3>Operational Commands</h3>
<h4>Uninstall n8n</h4>
<pre><code>./scripts/uninstall.sh</code></pre>

<h4>Cleanup Persistent Data</h4>
<pre><code>./scripts/cleanup.sh</code></pre>

<h4>Scale Down / Up</h4>
<pre><code>kubectl scale deployment n8n-stack-n8n-stack -n n8n-system --replicas=0
kubectl scale deployment n8n-stack-n8n-stack -n n8n-system --replicas=1
</code></pre>

<h3>Included AI Workflow</h3>
<p>This repo includes an AI-powered n8n workflow:</p>
<ul>
  <li><strong>Workflow file</strong>: <code>ai-workflow.json</code></li>
  <li><strong>Metadata</strong>: <code>ai-metadata.yml</code></li>
</ul>
<p>To use:</p>
<ol>
  <li>Import the <code>.json</code> into n8n via the UI</li>
  <li>Connect your API keys (e.g., OpenAI)</li>
  <li>Execute and customize as needed</li>
</ol>

<h3>References</h3>
<ul>
  <li><a href="https://docs.n8n.io/" target="_blank">n8n Official Docs</a></li>
  <li><a href="https://8gears.container-registry.com/" target="_blank">n8n Helm Chart Registry</a></li>
  <p>n8n kubernetes helm chart</p>
</ul>

<h3>Conclusion</h3>
<p>With this Helm-based setup, n8n can be deployed in a secure, scalable, and GitOps-friendly way. Whether you’re building simple integrations or advanced AI workflows, this approach gives you full control over automation infrastructure on Kubernetes.</p><div class="separator"><a href="/assets/images/original/2025/08/scaling-great-workflow-system-n8n-on/images.png" imageanchor="1"><img border="0" data-original-height="221" data-original-width="228" height="221" src="/assets/images/original/2025/08/scaling-great-workflow-system-n8n-on/images.png" width="228" /></a></div><p></p>
