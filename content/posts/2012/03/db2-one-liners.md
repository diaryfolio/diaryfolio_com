---
title: "db2 one liners"
date: "2012-03-19T16:53:00Z"
updated: "2014-06-22T17:25:40.386Z"
legacy_url: "/2012/03/db2-one-liners.html"
source_id: "tag:blogger.com,1999:blog-5931535581904587661.post-5344478015705548140"
author: "df"
labels:
  - "schema"
  - "db2 snapshot"
  - "check foreign keys"
  - "db2 export"
  - "db2 tables"
  - "db2look"
  - "db2 prompt"
  - "db2 constraints"
  - "Technology"
  - "foreign key references"
  - "db2 locks"
  - "db2 indexes"
---

Some very helpful one liners for db2.<br/><br/>If you are a fan like me to execute db2 commands within the Unix/AIX prompt, rather than going into DB2 inbuilt prompt then all commands run on the fly. Much powerful is Unix prompt as you can modify data in whichever way you want.<br/><blockquote><br/><ul><br/>	<li>db2 list database directory;    #Lists all databases within the installation</li><br/>	<li>db2 list node directory;</li><br/>	<li>db2 "SELECT SCHEMANAME FROM SYSCAT.SCHEMATA";  #Shows all schema within the Database Instance</li><br/>	<li>db2 set schema myschema01   # Setting schema before execution</li><br/>	<li>db2 "LIST TABLES FOR SCHEMA myschema01" | more</li><br/>	<li>db2 describe indexes for table &lt;table_name&gt; show detail | tr -s " "   # shows details about the table including primary key and indexes</li><br/>	<li>db2 get snapshot for application agentid 228 | more</li><br/>	<li># db2 "force applicatioin (228) "   #Careful as it forces the session 228 out of DB2</li><br/>	<li>db2pd -d myDB01 -wlocks</li><br/>	<li>db2 export to C:\CSVFiles\OutputmyTable.csv of del select * from myTable   #For exporting data into CSV files.</li><br/>	<li>db2 "VALUES CURRENT QUERY OPTIMIZATION"    # Checks the current optimisation level. Try changing and resetting it for your queries to run better</li><br/>	<li>db2look -d&lt;dbname&gt; -z &lt;schema&gt; -t &lt;table_name&gt; -a -e -o output.ddl    #db2look utility is very useful in duplicating table and structures . Plenty of <a href="http://publib.boulder.ibm.com/infocenter/db2luw/v9/index.jsp?topic=%2Fcom.ibm.db2.udb.admin.doc%2Fdoc%2Fr0002051.htm">flags available</a> including wildcards.</li><br/>	<li>db2 "select * from syscat.tabconst"                # To check table constraints</li><br/>	<li>db2 "select * from syscat.references"            # To check foreign key references of a table</li><br/>	<li>syscat.keyclouse (contraint details),   syscat.checks (contraints at schema level)</li><br/></ul><br/></blockquote>
