---
title: "VS Code & Portable GIT shell integration in Windows"
date: "2022-01-01T22:32:00.009Z"
updated: "2025-04-22T00:46:38.304Z"
legacy_url: "/2022/01/vs-code-portable-git-shell-integration.html"
source_id: "tag:blogger.com,1999:blog-5931535581904587661.post-736760545140876427"
author: "df"
labels:
  - "cygwin"
  - "git"
  - "VSCode"
  - "portable"
---

<h2>Summary</h2><p>Many of your corporate laptop cannot install programs and it is quite good to have them as portable executables. Here we find a way to have Portable VS Code and Portable GIT and integrate the GIT shell into VS Code</p><h2>Pre-Reqs</h2><p></p><ul><li>VS Code (Install version or <a href="https://code.visualstudio.com/sha/download?build=stable&amp;os=win32-x64-archive" target="_blank">Portable</a>)</li><li>GIT <a href="https://github.com/git-for-windows/git/releases/download/v2.34.1.windows.1/PortableGit-2.34.1-64-bit.7z.exe" target="_blank">portable</a></li></ul><p></p><h2>Steps</h2><p></p><ul><li>Create a directory in your Windows device (eg:&nbsp;<i>C:\installables\</i>)</li><li>Unpack GIT portable into the above directory (eg it becomes: <i>C:\installables\PortableGit</i>)</li><li>Now unpack Visual Studio (VS) Code and run it. The default shell would be windows based</li><li>Update User or Workspace settings of VS Code (ShortCut is:&nbsp;<i>Control+Shift+p</i> )</li><li>Search for 'Open Workspace Settings (JSON)' and press Enter <br /></li><li>Update the settings with following setting</li></ul>
<pre>    {<br />        "workbench.colorTheme": "Default Dark+",<br />        "git.ignoreMissingGitWarning": true,<br />        "git.enabled": true,<br />        "terminal.integrated.profiles.windows": {<br />           "git_bash"" { <br />              "path": "C:\\installables\\PortableGit\\bin\\bash.exe"<br />           } <br />         },<br />        "terminal.integrated.defaultProfile.windows": "git_bash"<br />     }</pre>
<div><ul><li>Now close the VS Code and reopen it and check for shell. You should have a Linux/bash type shell with git included</li></ul><div><br /></div></div><div class="separator"><a href="https://blogger.googleusercontent.com/img/a/AVvXsEiaObgSpHxjj7SyfkK68pp31zR73IUeEAjr6mvz_CHnzbfMvLaR733cv3zfFN9O1HthAjMSDWoLZGXxzeDtYHX_EE6aoxckJW6wQANUDuhsLIp4mBYhs5YOydDnJb9nFpXO0Qj5bPqFcen4_TRrEm7agDFL_l-o2eOlvBZnNRIX6bYTZyxDtClt2JeD=s840"><img border="0" data-original-height="440" data-original-width="840" height="336" src="https://blogger.googleusercontent.com/img/a/AVvXsEiaObgSpHxjj7SyfkK68pp31zR73IUeEAjr6mvz_CHnzbfMvLaR733cv3zfFN9O1HthAjMSDWoLZGXxzeDtYHX_EE6aoxckJW6wQANUDuhsLIp4mBYhs5YOydDnJb9nFpXO0Qj5bPqFcen4_TRrEm7agDFL_l-o2eOlvBZnNRIX6bYTZyxDtClt2JeD=w640-h336" width="640" /></a></div><br /><div><br /></div><p></p><p><br /></p>
