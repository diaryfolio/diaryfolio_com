---
title: "Birds-eye view of Kubernetes objects"
date: "2022-09-29T05:59:00.006Z"
updated: "2024-04-03T01:47:18.233Z"
legacy_url: "/2022/09/birds-eye-view-of-kubernetes-objects.html"
source_id: "tag:blogger.com,1999:blog-5931535581904587661.post-6115137822379618897"
author: "df"
labels:
  - "kubernetes"
  - "devops"
  - "PAAS"
---

<p>&nbsp;Kuberenetes has given a 'Software view' for the 'hardware' world. That too all resources consumed via modern definitions using json/yaml and via API.&nbsp;</p><p>Kuberentes segments the compute resources into Worker nodes &amp; Master Node(s) and contain persistent entities called 'Kubernetes Objects' including</p><p></p><ul><li>Containerised applications</li><li>Cluster and Associated nodes</li><li>Resources to these nodes</li><li>The policies and tolerances on how the applications interact and behave</li></ul><div><br /></div><div>Below is a good diagram of the various components</div><p></p><div class="separator"><a href="/assets/images/original/2022/09/birds-eye-view-of-kubernetes-objects/k8s1.jpeg"><img border="0" data-original-height="542" data-original-width="1046" height="333" src="/assets/images/original/2022/09/birds-eye-view-of-kubernetes-objects/k8s1.jpeg" width="640" /></a></div><br /><p><br /></p><p>Each component can be defined by software/code and scalable which makes kubernetes the de-facto building framework for modern micro-service applications.&nbsp;</p><p>In most of the scenarios the components can be tiered into&nbsp;</p><p></p><ul><li>Host/Virtual machines</li><li>Kuberentes Platform</li><li>Containers</li><li>Microservices</li></ul><p></p><div class="separator"><a href="/assets/images/original/2022/09/birds-eye-view-of-kubernetes-objects/kubernetes1.jpeg" imageanchor="1"><img border="0" data-original-height="612" data-original-width="529" height="400" src="/assets/images/original/2022/09/birds-eye-view-of-kubernetes-objects/kubernetes1.jpeg" width="346" /></a></div><div>It is hence very important to understand the difference between traditional 2 tier model and kuberentes 4 tier model for all your Operational, Security and Observability needs for a successful implementation.</div><p><br /></p>
