---
layout: page
permalink: /publications/
title: publications
description: An up-to-date list is available on <a href="https://scholar.google.com/citations?user=MasiEogAAAAJ&hl=en" title="Google Scholar"><i class="ai ai-google-scholar"></i></a>
years: [2024,2023,2022,2021,2020,2019,2018]
nav: true
nav_order: 1
---

<div class="publications">

{%- for y in page.years %}
  <h2 class="year">{{y}}</h2>
  {% bibliography -f papers -q @*[year={{y}}]* %}
{% endfor %}

</div>
