---
title: History of American Food Cultures
term: Summer 2019
number: HIST 413
layout: syllabus
header: american-food
slug: american-food
---

{% assign slug={{page.slug}} %}



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
  </div>
  {% endif %}   
{% endfor %}  
