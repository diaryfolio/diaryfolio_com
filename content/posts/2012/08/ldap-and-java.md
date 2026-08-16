---
title: "ldap and Java"
date: "2012-08-14T16:16:00Z"
updated: "2014-06-22T17:25:41.096Z"
legacy_url: "/2012/08/ldap-and-java.html"
source_id: "tag:blogger.com,1999:blog-5931535581904587661.post-3884858414998635621"
author: "df"
labels:
  - "InitialDirContext ldap"
  - "java and ldap"
  - "Technology"
  - "SearchControls ldap"
  - "ldap code"
---

For those who are starters with LDAP, a good article can be found in <a href="http://en.wikipedia.org/wiki/Lightweight_Directory_Access_Protocol">Wikipedia</a>.  The LDAP URL is fairly extensible and a sample format is<br/><blockquote>ldap://host:port/DN?Atributes_to_Fetch?range?SearchFilter?extensions<br/><ul><br/>	<li>hostname is the Fully Qualified (FQDN) or IP address of the LDAP server to search.</li><br/>	<li>port is the network port (default port 389) of the LDAP server.</li><br/>	<li>DN is the distinguished name to use as the search base.</li><br/>	<li>Atributes_to_Fetch is comma-separated.</li><br/>	<li>range specifies the search scope and can be "base" (the default), "one" or "sub".</li><br/>	<li>SearchFilter is a search critiera. Can accept wild characters too</li><br/>	<li>extensions are optional.</li><br/></ul><br/></blockquote><br/>A sample ldap program in Java<br/><blockquote>import javax.naming.directory.*;<br/>import javax.naming.*;<br/>import java.util.Vector;<br/>import java.util.Enumeration;<br/>import java.util.Properties;<br/>public class search {<br/>public static void main(String[] args) {<br/>String base = "cn=generic,ou=MyClient,ou=Applications,ou=Pacific,o=mycompany.net";<br/>String filter = "(uniquemember=uid=myuserid,ou=Users,ou=Pacific,o=mycompany.net)";<br/>Properties env = new Properties();<br/>env.put(DirContext.INITIAL_CONTEXT_FACTORY,   "com.sun.jndi.ldap.LdapCtxFactory");<br/>env.put(DirContext.PROVIDER_URL,"ldap://10.123.34.56:44389");<br/>env.put( Context.SECURITY_PRINCIPAL, "uid=myuserid,ou=Users,ou=Pacific,o=mycompany.net" );<br/>env.put( Context.SECURITY_CREDENTIALS, "passkey" );<br/><br/>try {<br/>DirContext dc = new InitialDirContext(env);<br/>SearchControls sc = new SearchControls();<br/>sc.setSearchScope(SearchControls.OBJECT_SCOPE);<br/>NamingEnumeration ne = null;<br/>ne = dc.search(base, filter, sc);<br/>while (ne.hasMore()) {<br/>SearchResult sr = (SearchResult) ne.next();<br/>System.out.println(sr.toString()+"\n");<br/>}<br/>dc.close();<br/>} catch (NamingException nex) {<br/>System.err.println("Error: " + nex.getMessage());<br/>}<br/>}<br/>}</blockquote><br/>Print's Details of the directory structure<br/><br/>&nbsp;<br/><br/>[ad#ad-2]
