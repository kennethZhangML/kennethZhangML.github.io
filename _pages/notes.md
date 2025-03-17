---
layout: page
title: notes
permalink: /notes/
description: Personal-study notes for quant-finance related learning materials 
nav: true
nav_order: 6
display_categories: [notes]
horizontal: false
---

## Disclaimer: There are issues in generating the TeX math used in my notes, I am currently working to fix it. Thanks!
<div class="notes">
{% assign sorted_notes = site.notes | where_exp: "note", "note.parent == nil" | sort: "importance" %}

<div class="container">
  <div class="row justify-content-center gx-3 gy-3">
    {% for note in sorted_notes %}
      <div class="col-md-4 d-flex">
        <div class="card flex-fill">
          {% if note.img %}
            <img src="{{ site.baseurl }}/{{ note.img }}" alt="{{ note.title }}" class="card-img">
          {% endif %}
          <h3><a href="{{ note.url }}">{{ note.title }}</a></h3>
          <p>{{ note.description }}</p>
        </div>
      </div>
    {% endfor %}
  </div>
</div>
</div>
