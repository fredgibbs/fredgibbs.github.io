---
layout: default
title: posters | fred gibbs
permalink: /portfolio/flyers/
---

# Poster Gallery

<div class="gallery-container">
<div class="poster-gallery" id="posterGallery">
  {% for poster in site.data.posters %}
  <button type="button" class="poster-thumb-button" data-full-src="images/{{ poster.filename }}.jpg" aria-label="Open poster">
    <img src="thumbs/{{ poster.filename }}.png" class="poster-thumb" alt="Poster">
  </button>
  {% endfor %}
</div>
</div>

<dialog id="posterDialog" class="poster-dialog" aria-label="Poster preview">
  <button type="button" class="poster-dialog-close" id="posterDialogClose" aria-label="Close poster preview">×</button>
  <img id="posterDialogImage" src="" alt="Poster preview">
</dialog>

<script>
document.addEventListener('DOMContentLoaded', function () {
  var gallery = document.getElementById('posterGallery');
  var dialog = document.getElementById('posterDialog');
  var dialogImage = document.getElementById('posterDialogImage');
  var closeButton = document.getElementById('posterDialogClose');

  if (!gallery || !dialog || !dialogImage || !closeButton) return;

  gallery.addEventListener('click', function (event) {
    var button = event.target.closest('.poster-thumb-button');
    if (!button) return;

    var fullSrc = button.getAttribute('data-full-src');
    if (!fullSrc) return;

    dialogImage.src = fullSrc;

    if (typeof dialog.showModal === 'function') {
      dialog.showModal();
    } else {
      window.open(fullSrc, '_blank');
    }
  });

  closeButton.addEventListener('click', function () {
    dialog.close();
  });

  dialog.addEventListener('click', function (event) {
    var bounds = dialog.getBoundingClientRect();
    var isOutside = (
      event.clientX < bounds.left ||
      event.clientX > bounds.right ||
      event.clientY < bounds.top ||
      event.clientY > bounds.bottom
    );

    if (isOutside) {
      dialog.close();
    }
  });
});
</script>
