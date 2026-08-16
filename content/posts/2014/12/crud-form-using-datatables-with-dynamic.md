---
title: "CRUD form using Datatables with dynamic Add & Delete rows"
date: "2014-12-08T19:45:00.003Z"
updated: "2015-04-24T12:16:35.370Z"
legacy_url: "/2014/12/crud-form-using-datatables-with-dynamic.html"
source_id: "tag:blogger.com,1999:blog-5931535581904587661.post-2749521680685059774"
author: "df"
labels:
  - "crud"
  - "datatables"
  - "Web development"
  - "JSON"
  - "ajax"
  - "jquery"
---

<div dir="ltr" trbidi="on">
<div dir="ltr" trbidi="on">
Hope you guys have suffered same issues as me with Web Development to create forms with Create/Read/Update/Delete functionality. I really use "Datatables" (<a href="http://www.datatables.net/">www.datatables.net</a>) for displaying data in tabular format. &nbsp;Datatables has got many advantages and is easily compatible with bootstrap stylings.<br />
<div class="separator">
<a href="/assets/images/original/2014/12/crud-form-using-datatables-with-dynamic/CRUD.gif" imageanchor="1"><img border="0" src="/assets/images/original/2014/12/crud-form-using-datatables-with-dynamic/CRUD.gif" height="163" width="200" /></a></div>
<br />
<ul>
<li>IE8+ support, major browser support and uses jQuery as its core</li>
<li>Can natively map JSON data</li>
<li>Searching and Filtering functionality with pagination Support</li>
<li>MultiLanguage support, ClientSide Sorting, AJAX based inputs</li>
<li>Can filter required Columns at front-end</li>
</ul>
<div>
Datatables is free but it's editor (editable tables) are paid. Hence I thought of putting together a simple table to use for editing and publishing data for POST purposes.</div>
<div>
In Summary, what we are doing here is<br />
<ul>
<li>Creating HTML stub with table headers within a <i>form</i>. Also add "Add Row" and "Delete Row" buttons with <i>onclick </i>actions attached to it and a "Submit" button</li>
<li>In your javascript, "<i>on document load</i>" create a datatable with built in "<i>input=text</i>" form for rows. This can be done using&nbsp;<i>fnAddData</i>
<pre>    function addRow() {
      $('table#myTable').dataTable().fnAddData([
        'input type="text" class="first_name" id="first_name_' + count + '"&gt;',   // Note the class name
        'input type="text" class="last_name" id="last_name_' + count + '"&gt;'
      ]);

      count++;
    }
</pre>
</li>
<li>Similarly for "Delete Row" action, bind it to &nbsp; <pre> $("table#myTable").dataTable().fnDeleteRow(count - 1);</pre>
</li>
<li>Using "Add Row" and "Delete Row" you can add/remove any number of rows.</li>
<li>When you Click the Submit button, the dataTable is scanned and fetched as Key-Value object pair. This is pushed into a JSON object Array.</li>
<pre>      $("#submitButton").click(function() {
        oTable = $('#myTable').dataTable();
        var numColumns = oTable.fnGetData(0).length;
        var rules = [];                                     

        $.each(oTable.fnGetData(), function(i, row) {
          var rec = {};
          for (var c = 0; c &lt; numColumns; c++) {
           // Extracting Class name as KEY
            var key = ($(row[c]).attr('class'));  
           // Dynamic Rows as VALUE          
            var value = ($('#' + key + '_' + i).val());     
            rec[key] = value;
          }
          rules.push(rec);

        })

        alert(JSON.stringify(rules));


      });
</pre>
</ul>
</div>
<div>
<br /></div>
<div>
Below is Sample of editable Datatables</div>
</div>
<iframe allowfullscreen="allowfullscreen" frameborder="0" src="https://embed.plnkr.co/gUBqIHEEmEaJ1Hmdwvoj" title="CRUD form demonstration" loading="lazy">
  Loading plunk...
</iframe><br />
<br />
Pure web-based create/read/update/delete (CRUD) table with AJAX post functionality</div>
