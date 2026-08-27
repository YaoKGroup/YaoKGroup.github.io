---
layout: page
title: "相册"
subtitle: ""
permalink: /zh/gallery/
lang: zh
en_url: /gallery/
---

<div id="custom-gallery-container">
  <style>
    #custom-gallery-container { color: var(--text-main); }
    #custom-gallery-container .gallery-filters { display: flex; gap: 30px; margin: 20px 0 40px 0; border-bottom: 1px solid #eee; padding-bottom: 15px; }
    #custom-gallery-container .filter-tag { font-size: 1.1rem; text-transform: none; cursor: pointer; color: var(--ust-blue); padding: 5px 0; transition: color 0.2s ease; position: relative; font-weight: 600; }
    #custom-gallery-container .filter-tag:hover, #custom-gallery-container .filter-tag.active { color: var(--gold); }
    #custom-gallery-container .filter-tag.active { font-weight: 500; }
    #custom-gallery-container .filter-tag::after { content: ''; position: absolute; bottom: -16px; left: 0; width: 100%; height: 3px; background: var(--gold); transform: scaleX(0); transform-origin: center; transition: transform 0.2s ease; }
    #custom-gallery-container .filter-tag.active::after { transform: scaleX(1); }
    #custom-gallery-container .gallery-grid { display: block; column-count: 3; column-gap: 20px; width: 100%; }
    @media (max-width: 900px) { #custom-gallery-container .gallery-grid { column-count: 2; } }
    @media (max-width: 600px) { #custom-gallery-container .gallery-grid { column-count: 1; } }
    #custom-gallery-container .gallery-item { display: inline-block; width: 100%; margin-bottom: 20px; break-inside: avoid; position: relative; border-radius: 10px; overflow: hidden; background: #f9f9f9; transition: opacity 0.4s ease; }
    #custom-gallery-container .gallery-item.hidden { display: none; }
    #custom-gallery-container .gallery-item img { width: 100%; height: auto; display: block; transition: transform 0.3s ease; }
    #custom-gallery-container .gallery-overlay { position: absolute; bottom: 0; left: 0; right: 0; background: linear-gradient(to top, rgba(0,0,0,0.85) 0%, rgba(0,0,0,0) 100%); color: #fff; padding: 15px 12px 8px 12px; opacity: 0; transform: translateY(5px); transition: all 0.3s ease; pointer-events: none; z-index: 2; }
    #custom-gallery-container .gallery-item:hover .gallery-overlay { opacity: 1; transform: translateY(0); }
    #custom-gallery-container .gallery-item:hover img { transform: scale(1.05); }
    .overlay-title { font-family: inherit; font-size: 1rem; font-weight: 500; display: block; margin: 0 0 2px 0; padding: 0; line-height: 1.15; }
    .overlay-desc { font-family: inherit; font-size: 0.8rem; opacity: 0.9; display: block; line-height: 1.2; margin: 0; padding: 0; }
  </style>

  <div class="gallery-filters">
    <span class="filter-tag active" data-filter="all">全部</span>
    <span class="filter-tag" data-filter="media">媒体报道</span>
    <span class="filter-tag" data-filter="moments">瞬间</span>
    <span class="filter-tag" data-filter="captures">摄影</span>
  </div>

  <div class="gallery-grid" id="gallery-grid">
    <div class="gallery-item" data-category="moments">
      <img src="{{ site.baseurl }}/photos/moments/260827 ISD ori.jpg" alt="260827">
      <div class="gallery-overlay">
        <span class="overlay-title">ISD 新生见面会</span>
        <span class="overlay-desc">姚教授上台进行自我介绍</span>
      </div>
    </div>
    <div class="gallery-item" data-category="moments">
      <img src="{{ site.baseurl }}/photos/moments/260825 RI lecture.jpg" alt="260825">
      <div class="gallery-overlay">
        <span class="overlay-title">CKSRI 研讨会</span>
        <span class="overlay-desc">面向触觉、机器人感知与医疗健康的柔性电子系统</span>
      </div>
    </div>
    <div class="gallery-item" data-category="moments">
      <img src="{{ site.baseurl }}/photos/moments/2026-group-photo.jpg?v=20260822" alt="YAO课题组合影">
      <div class="gallery-overlay">
        <span class="overlay-title">课题组合影</span>
        <span class="overlay-desc">YAO Research Group 聚餐留影</span>
      </div>
    </div>
    <div class="gallery-item" data-category="media">
      <img src="{{ site.baseurl }}/photos/media/arn.png" alt="Asia Research News">
      <div class="gallery-overlay">
        <span class="overlay-title">Asia Research News</span>
        <span class="overlay-desc">超薄无线掌心贴片将触觉带入虚拟现实</span>
      </div>
    </div>
    <div class="gallery-item" data-category="media">
      <img src="{{ site.baseurl }}/photos/media/TVB.png" alt="TVB HK">
      <div class="gallery-overlay">
        <span class="overlay-title">TVB HK</span>
        <span class="overlay-desc">城大研发电子皮肤触感反馈技术 冀提升虚拟实境体验</span>
      </div>
    </div>
    <div class="gallery-item" data-category="captures">
      <img src="{{ site.baseurl }}/photos/cpt/YKM1194.jpg" alt="YKM1194">
    </div>
    <div class="gallery-item" data-category="captures">
      <img src="{{ site.baseurl }}/photos/cpt/YKM1216.jpg" alt="YKM1216">
    </div>
    <div class="gallery-item" data-category="moments">
      <img src="{{ site.baseurl }}/photos/moments/260516.jpeg" alt="260516">
      <div class="gallery-overlay">
        <span class="overlay-desc">南北小廚的晚餐</span>
      </div>
    </div>
    <div class="gallery-item" data-category="captures">
      <img src="{{ site.baseurl }}/photos/cpt/YKM1514.jpg" alt="YKM1514">
    </div>
    <div class="gallery-item" data-category="captures">
      <img src="{{ site.baseurl }}/photos/cpt/YKM1231.jpg" alt="YKM1231">
    </div>
    <div class="gallery-item" data-category="captures">
      <img src="{{ site.baseurl }}/photos/cpt/YKM240919.jpg" alt="YKM240919">
    </div>
  </div> 

  <script>
    document.addEventListener("DOMContentLoaded", function() {
      const filters = document.querySelectorAll('#custom-gallery-container .filter-tag');
      const items = document.querySelectorAll('#custom-gallery-container .gallery-item');
      filters.forEach(filter => {
        filter.addEventListener('click', function() {
          filters.forEach(f => f.classList.remove('active'));
          this.classList.add('active');
          const selectedFilter = this.getAttribute('data-filter');
          items.forEach(item => {
            const itemCategory = item.getAttribute('data-category');
            if (selectedFilter === 'all' || selectedFilter === itemCategory) {
              item.classList.remove('hidden');
            } else {
              item.classList.add('hidden');
            }
          });
        });
      });
    });
  </script>
</div>
