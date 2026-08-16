---
title: "Identity management and Open source alternatives"
date: "2012-08-20T11:24:00Z"
updated: "2014-11-21T00:19:21.464Z"
legacy_url: "/2012/08/identity-management-and-open-source.html"
source_id: "tag:blogger.com,1999:blog-5931535581904587661.post-7207562497065762214"
author: "df"
labels:
  - "enterprise Single Sign-on"
  - "identity management"
  - "Open source alternative siteminder"
  - "esso"
  - "Technology"
---

<div dir="ltr" trbidi="on">
Identity Management has become a critical component in modern IT industry. Its a challenge to choose the best product, while ensuring the flexibility is not lost due to increase in employee base and adhering to security compliance needs. Some of the key industry leading products include CA Siteminder, Oracle Access&nbsp; Manager, IBM Tivoli Access Manager and so on. Before explaining the products and alternatives, let's analyze the different capabilities required for an IT enterprise.<br />
<br />
Identity management solution normally requires <strong>Access Management, Federation, Web Services Ability, Policy Based Enforcements, Enterprise Single Sign on (ESSO)</strong> and so on. Let's see a sample Comparison table for each of the products<br />
<br />
<h2>
Comparison of Major Identity management solutions</h2>
<br /><table border="0" cellpadding="0" cellspacing="0"><colgroup> <col width="154"></col> <col width="102"></col> <col width="104"></col> <col width="123"></col> </colgroup><tbody>
<tr><td height="51" width="154"></td><td width="102"><strong>CA Siteminder</strong></td><td width="104"><strong>Oracle Access Manager</strong></td><td width="123"><strong>IBM Tivoli Access Manager</strong></td></tr>
<tr><td height="17"><strong>Access Management</strong></td><td width="102"><span>Yes</span></td><td width="104"><span>Yes</span></td><td width="123"><span>Yes</span></td></tr>
<tr><td height="34"><strong>Federation</strong></td><td width="102">Require Federation Mgr</td><td width="104">Oracle Identity Federation</td><td width="123">Federated Identity Mgr</td></tr>
<tr><td height="34"><strong>Web Services Support</strong></td><td width="102">CA WS Manager</td><td width="104">WS Manager</td><td width="123">Federated Identity Mgr</td></tr>
<tr><td height="51"><strong>Policy Enforcements</strong></td><td width="102">CA Entitlements Mgr</td><td width="104">Oracle Entitlements Mgr</td><td width="123">Security Policy Mgr</td></tr>
<tr><td height="34"><strong>Enterprise SSO</strong></td><td width="102">CA Single Sign-on</td><td width="104">Passlogix</td><td width="123">Access Manager Adapter</td></tr>
</tbody></table>
<br />
<br />
<h2>
<strong>&nbsp;So What are the Open Source Alternatives?</strong></h2>
<br />
<ol>
<li><a href="http://www.openldap.org/" target="_blank">OpenLDAP </a>- Mostly a LDAP implementation, but available with most of native OS installations. Now an essential part of CURL</li>
<br />
<li><a href="https://cwiki.apache.org/confluence/display/KNOX/Designs" target="_blank">Apache Knox</a> -&nbsp;provides pluggable authentication to LDAP using REST API's. Knox would be fast growing especially in big data environments<br /><table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container"><tbody>
<tr><td><img alt="" src="http://hortonworks.com/wp-content/uploads/2013/10/knox1.jpg" height="342" width="453" /></td></tr>
<tr><td class="tr-caption"><span>Apache Knox Design</span></td></tr>
</tbody></table>
</li>
<li><a href="http://www.forgerock.com/openam.html" target="_blank">OpenAM </a>- The forked version of the ever best OpenSSO project which was dismantled after Oracle's bid on Sun.&nbsp; Some great documentation and <a href="https://wikis.forgerock.org/confluence/display/openam/Home" target="_blank">Video Tutorials&nbsp; </a>for beginners.</li>
<br />
<li><a href="http://www.simplesamlphp.org/" target="_blank">SimpleSAMLphp</a>- If you are working on PHP clients, this one is for you. A native PHP based simple tool.</li>
<br />
<li><a href="http://opends.java.net/" target="_blank">OpenDS </a>- Not so active thesedays.</li>
<br />
<li>Others include&nbsp; <a href="http://openliberty.org/" target="_blank">OpenLiberty</a>,<a href="http://lasso.entrouvert.org/" target="_blank"> Lasso</a>, <a href="http://www.eclipse.org/higgins/" target="_blank">Higgins Project</a> from Eclipse</li>
</ol>
<br />
<br />
<br />
</div>
