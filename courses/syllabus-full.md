---
title: National Historic Trails
term: Fall 2018
number: HIST 300
layout: syllabus
header: trails
---

{% assign slug={{page.header}} %}

{% for page in site.pages %}
  {% if page.header == slug and page.section == "home" %}
  <div>
  <h1>General Information</h1>
  {{page.content}}
  </div>
  {% endif %}  

  {% if page.header == slug and page.section == "schedule" %}


  <div>
  <hr/><hr/>
    <h1>Schedule, Readings and Due Dates<h1>
    {{page.content}}

  {% endif %}   
{% endfor %}  
