---
title: "IMDB API&#39;s and URL based search parameters"
date: "2014-05-31T21:12:00Z"
updated: "2014-11-21T00:54:30.371Z"
legacy_url: "/2014/05/imdb-api-and-url-based-search-parameters.html"
source_id: "tag:blogger.com,1999:blog-5931535581904587661.post-2937617759587066710"
author: "df"
labels:
  - "api"
  - "imdb"
  - "Technology"
---

<div dir="ltr" trbidi="on">
<h2>
<span>
Advanced Search in IMDB</span></h2>
<br />
I'm a big fan of IMDB and everytime if you really want to do detailed search, you need to use <a href="http://www.imdb.com/search/title" target="_blank">IMDB Advanced Search</a>. But this is not practical each time, but seems you could tweak IMDB URL's to do magic searches.<br />
<div class="separator">
<a href="http://img4.wikia.nocookie.net/__cb20130730023210/godzilla/images/f/f2/IMDb.png" imageanchor="1"><img border="0" src="http://img4.wikia.nocookie.net/__cb20130730023210/godzilla/images/f/f2/IMDb.png" height="199" width="320" /></a></div>
<br />
Few examples below.&nbsp;If you look the search tag, everything is self explanatory<br />
<h4>
<ul>
<li>Most Popular English/Hindi-Language Feature Films Released 1 January 1980 Or Later With User Rating Between 7.5 And 10 and At Least 500 Votes</li>
</ul>
</h4>
<pre>http://www.imdb.com/search/title?languages=en,hi&amp;num_votes=500,&amp;release_date=1980-01-01,&amp;title_type=feature&amp;user_rating=7.5,</pre>
<h4>
<ul>
<li>Highest Rated Feature Films Not In "watchlist" Released 2011 Or Later With At Least 5,000 Votes</li>
</ul>
</h4>
<pre>http://www.imdb.com/search/title?num_votes=5000,&amp;release_date=2011,&amp;sort=user_rating,desc,&amp;title_type=feature&amp;my_ratings=exclude&amp;lists=!watchlist</pre>
<h4>
<ul>
<li>IMDB Top TV Series - Highest Rated TV Series With At Least 2,000 Votes</li>
</ul>
</h4>
<pre>http://www.imdb.com/search/title?num_votes=2000,&amp;sort=user_rating,desc&amp;title_type=tv_series</pre>
<h4>
<ul>
<li>Highest Rated Action Feature Films Released In 2013</li>
</ul>
</h4>
<pre>http://www.imdb.com/search/title?at=0&amp;genres=action&amp;sort=user_rating&amp;title_type=feature&amp;year=2013,2013</pre>
<h4>
<ul>
<li>Now a more complex one:&nbsp;Most Popular ----&gt;United States-G/United States-PG/United States-PG-13/United States-R/United States-NC-17 ----&gt;Color ----&gt;DTS ----&gt;IMDb "Top 1000" ----&gt;English-Language ----&gt;Action-Thriller ----&gt;TV Movies ----&gt;Released 1 January 2000 to 1 January 2014 ----&gt;US Box Office Between $100,000 And $200,000,000 ----&gt;20,000-100,000 Votes, ----&gt;Country of Origin United States, ----&gt;User Rating Between 8.4 And 9.2 , ----&gt;20th Century Fox Among Companies And Sony Among Companies And DreamWorks Among Companies And Paramount Among Companies , ----&gt;Production Status: Released ----&gt;Starring: Leonardo DiCaprio</li>
</ul>
</h4>
<pre>http://www.imdb.com/search/title?boxoffice_gross_us=100000,200000000&amp;certificates=us:g,us:pg,us:pg_13,us:r,us:nc_17&amp;colors=color&amp;companies=fox,columbia,dreamworks,paramount&amp;countries=us&amp;genres=action,thriller&amp;groups=top_1000&amp;has=alternate-versions,awards,asin-blu-ray-ca,asin-blu-ray-us,asin-blu-ray-de,asin-blu-ray-fr,asin-blu-ray-uk,asin-hardcover-ca,asin-hardcover-us&amp;languages=en&amp;num_votes=20000,100000&amp;production_status=released&amp;release_date=2000-01-01,2014-01-01&amp;role=nm0000138&amp;sound_mixes=dts&amp;title_type=tv_movie&amp;user_rating=8.4,9.2</pre>
<br />
<h2>
Pure API</h2>
For developers, a good list of API's can be found in <a href="https://www.blogger.com/%20http://stackoverflow.com/questions/1966503/does-imdb-provide-an-api" target="_blank">this Stackoverflow Question</a></div>
