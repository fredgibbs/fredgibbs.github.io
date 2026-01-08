---
layout: default
title: posters | fred gibbs
---

# Poster Gallery

<div class="container mt-4">
  <div class="row g-3">
    {% for poster in site.data.posters %}
    <div class="col-md-4 col-sm-6">
      <a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" 
         onclick="document.getElementById('modalImage').src='images/{{ poster.filename }}.jpg'; return false;">
        <img src="thumbs/{{ poster.filename }}.png" class="img-fluid img-thumbnail" alt="Poster">
      </a>
    </div>
    {% endfor %}
  </div>
</div>

<!-- Image Modal - Full viewport -->
<div class="modal fade" id="imageModal" tabindex="-1">
  <div class="modal-dialog modal-fullscreen">
    <div class="modal-content bg-dark">
      <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal"></button>
      <div class="modal-body d-flex align-items-center justify-content-center p-0">
        <img id="modalImage" src="" class="img-fluid" style="max-height: 100vh; cursor: zoom-in;" alt="">
      </div>
    </div>
  </div>
</div>
