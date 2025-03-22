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
**Note**: The scope of my engagement with *Stochastic Calculus for Finance* Volumes I & II by Steven E. Shreve has been curated to align with the analytical and modeling requirements typical of buy-side quantitative research. Accordingly, I have exercised discernment in omitting select chapters that either overlap with material addressed elsewhere or predominantly pertain to sell-side specializations. Specifically, in Volume I, Chapters 5 and 6 have been deliberately excluded, as their foundational content is revisited and treated with greater mathematical rigor in Volume II. Furthermore, I have chosen to omit Chapters 5, 7, 9, and 10 in Volume II, as these chapters primarily concern interest rate modeling, mortgage-backed securities, and fixed income derivatives—topics more germane to sell-side desks or fixed-income-centric roles. That said, I acknowledge that certain methodologies, such as the *Change of Numéraire* technique discussed in Chapter 10, retain theoretical relevance across asset classes, including select buy-side applications such as the valuation of exotic derivatives or structured products with interest rate components. Nevertheless, the primary objective of these notes is to distill the stochastic calculus frameworks and derivative pricing paradigms most pertinent to equity derivatives, volatility modeling, and other risk-neutral valuation approaches germane to the buy-side context.

**Disclaimer**: There are issues in generating the TeX math used in my notes, I am currently working to fix it. Thanks!
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
