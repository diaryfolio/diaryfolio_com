---
title: "db2top utility"
date: "2012-03-19T16:42:00Z"
updated: "2014-06-22T17:25:40.347Z"
legacy_url: "/2012/03/db2top-utility.html"
source_id: "tag:blogger.com,1999:blog-5931535581904587661.post-3570137327337934753"
author: "df"
labels:
  - "dynamic queries"
  - "db2top"
  - "Technology"
  - "db2user"
  - "db2 sessions"
---

Recently I had learnt about a great utility within DB2 to view the dynamic queries and session details.  The utility is called "<strong>db2top</strong>"   (Careful db2stop will stop DB !!)<br/><br/>To access it<br/><blockquote>1. Login to db2 user..  (say db2iuser1)<br/>2. db2top -d myDB  # myDB is my database name<br/>3. click on "l" key. It will show all the sessions hitting the database<br/>4. Click on "a" key to interrogate a specific session. And enter the session number shown in above screen<br/>5. Press "f" to force the session out. (Be careful). You might need to try twice as sometimes the session might come up again.<br/><br/>Enter key is for "action" and "refresh" etc.</blockquote><br/>Ensure that the command is not let run continously, as it takes fair bit of memory in long run.<br/><br/>A good <a href="http://publib.boulder.ibm.com/infocenter/db2luw/v9r5/index.jsp?topic=%2Fcom.ibm.db2.luw.admin.cmd.doc%2Fdoc%2Fr0025222.html">quide within IBM</a>  is for command line execution, and also with batch mode options.<br/><br/>&nbsp;
