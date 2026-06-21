---
layout: page
title: notes
permalink: /notes/
description: A curated-list of my notes
nav: true
nav_order: 6
display_categories: [notes]
horizontal: false
---

<div class="notes-container">

{% assign note_pdfs = site.static_files | where_exp: "file", "file.path contains '/_notes/'" | sort: "name" %}

{% for pdf in note_pdfs %}
  {% if pdf.extname == ".pdf" %}
    {% assign note_title = pdf.basename | replace: "-", " " | replace: "_", " " %}

    <details class="note-card">
      <summary>
        <span class="note-title">{{ note_title }}</span>
        <span class="note-meta">PDF notes</span>
      </summary>

      <div
        class="pdf-viewer"
        data-pdf-url="{{ pdf.path | relative_url }}"
      ></div>
    </details>
  {% endif %}
{% endfor %}

</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.min.js"></script>

<script>
  pdfjsLib.GlobalWorkerOptions.workerSrc =
    "https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js";

  async function renderPDF(container) {
    if (container.dataset.rendered === "true") {
      return;
    }

    container.dataset.rendered = "true";

    const url = container.dataset.pdfUrl;
    const pdf = await pdfjsLib.getDocument(url).promise;

    for (let pageNumber = 1; pageNumber <= pdf.numPages; pageNumber++) {
      const page = await pdf.getPage(pageNumber);

      const containerWidth = container.clientWidth - 24;
      const unscaledViewport = page.getViewport({ scale: 1 });
      const scale = containerWidth / unscaledViewport.width;
      const viewport = page.getViewport({ scale: scale });

      const canvas = document.createElement("canvas");
      const context = canvas.getContext("2d");

      canvas.width = viewport.width;
      canvas.height = viewport.height;
      canvas.className = "pdf-page";

      container.appendChild(canvas);

      await page.render({
        canvasContext: context,
        viewport: viewport
      }).promise;
    }
  }

  document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".note-card").forEach(function (card) {
      card.addEventListener("toggle", function () {
        if (card.open) {
          const viewer = card.querySelector(".pdf-viewer");
          renderPDF(viewer);
        }
      });
    });
  });
</script>

<style>
.notes-container {
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
}

.note-card {
  width: 100%;
  border: 1px solid var(--global-divider-color);
  border-radius: 10px;
  padding: 1rem 1.25rem;
  background: var(--global-card-bg-color);
}

.note-card summary {
  cursor: pointer;
  list-style: none;
  display: flex;
  justify-content: space-between;
  align-items: baseline;
}

.note-card summary::-webkit-details-marker {
  display: none;
}

.note-card summary::before {
  content: "▸";
  margin-right: 0.75rem;
  display: inline-block;
  transition: transform 0.15s ease;
}

.note-card[open] summary::before {
  transform: rotate(90deg);
}

.note-title {
  font-size: 1.35rem;
  font-weight: 500;
}

.note-meta {
  font-size: 0.9rem;
  opacity: 0.65;
}

.pdf-viewer {
  margin-top: 1.25rem;
  height: 80vh;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
  padding: 0.75rem;
  border: 1px solid var(--global-divider-color);
  border-radius: 8px;
}

.pdf-page {
  width: 100%;
  height: auto;
  border: 1px solid var(--global-divider-color);
  border-radius: 8px;
  background: white;
}
</style>