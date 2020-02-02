---
layout: default
title: posters | fred gibbs
---

<!-- <a data-fancybox="gallery" href="big_1.jpg"><img src="small_1.jpg"></a> -->

# Poster Gallery
<div class="row">

{% for poster in site.data.posters %}
<div class="col-mb-4">
  <a class="thumbnail" data-fancybox="gallery" href="images/{{ poster.filename }}.jpg">
  <img class="thumbnail" src="thumbs/{{ poster.filename }}.png"></a>
</div>
{% endfor %}

</div>
