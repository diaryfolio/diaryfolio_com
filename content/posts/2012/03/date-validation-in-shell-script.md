---
title: "Date Validation in a Shell Script"
date: "2012-03-06T12:35:00Z"
updated: "2014-06-22T17:25:40.014Z"
legacy_url: "/2012/03/date-validation-in-shell-script.html"
source_id: "tag:blogger.com,1999:blog-5931535581904587661.post-4576857039689723899"
author: "df"
labels:
  - "Technology"
---

Well I had numerous occasions to verify something at input of a ksh script.  This could be a date or number of particular string etc.<br/>The most useful commands here are  "grep -E -q"  which returns a return code based on the search condition.  Exploiting this logic, please find sample Date Validation check in ksh shell script<br/><blockquote># Date should fall in 2010-01-01  to 2019-12-31<br/># Script expecting a Date parameter in YYYYMMDD format as input<br/># This is not a 100% check, but will cover 99% of the scenario's<br/><br/>if [ $# -eq 1 ]<br/>then<br/>echo ${DateFormatInput} | grep -E -q '^201[1-9][01][0-9][0-3][0-9]$'<br/>if [[ $? != 0 ]]; then<br/>echo "Please enter Date in YYYYMMDD format. You Entered $@ "<br/>echo "Quitting.. No action done..."<br/>exit 0<br/>fi<br/>else<br/>echo "Please enter Date as parameter in YYYYMMDD format"<br/>echo "Quitting.. No action done..."<br/>exit 0<br/>fi</blockquote><br/>This script is useful especially when users enter various formats of date. Like UK employees use dd/mm/yyyy and some use mmddyyyy or some use yymmdd. This check will make users consistent in all your scripts.<br/>grep -E -q '^201[1-9][01][0-9][0-3][0-9]$'<br/>^ -&gt; shows it should start with 201<br/>$ -&gt; means it should end with [0-9] character
