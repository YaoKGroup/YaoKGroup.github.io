---
layout: page
title: "Gallery"
subtitle: ""
permalink: /gallery/
---

<div id="custom-gallery-container">
  <style>
    #custom-gallery-container {
      color: var(--text-main);
    }
    
    #custom-gallery-container .gallery-filters {
      display: flex;
      gap: 30px;
      margin: 20px 0 40px 0;
      border-bottom: 1px solid #eee;
      padding-bottom: 15px;
    }

    #custom-gallery-container .filter-tag {
      font-size: 1.1rem;
      text-transform: capitalize;
      cursor: pointer;
      color: var(--ust-blue);
      padding: 5px 0;
      transition: color 0.2s ease;
      position: relative;
      font-weight: 600;
    }

    #custom-gallery-container .filter-tag:hover,
    #custom-gallery-container .filter-tag.active { 
      color: var(--gold);
    }

    #custom-gallery-container .filter-tag.active { 
      font-weight: 500; 
    }

    #custom-gallery-container .filter-tag::after {
    content: '';
    position: absolute;
    bottom: -16px;
    left: 0;
    width: 100%;
    height: 3px;
    background: var(--gold);
    transform: scaleX(0);
    transform-origin: center;
    transition: transform 0.2s ease;
    }
  
    #custom-gallery-container .filter-tag.active::after {
      transform: scaleX(1);
    }

    #custom-gallery-container .gallery-grid {
      display: block;
      column-count: 3;
      column-gap: 20px;
      width: 100%;
    }

    @media (max-width: 900px) { #custom-gallery-container .gallery-grid { column-count: 2; } }
    @media (max-width: 600px) { #custom-gallery-container .gallery-grid { column-count: 1; } }

    #custom-gallery-container .gallery-item {
      display: inline-block;
      width: 100%;
      margin-bottom: 20px;
      break-inside: avoid;
      position: relative;
      border-radius: 10px;
      overflow: hidden;
      background: #f9f9f9;
      transition: opacity 0.4s ease;
    }

    #custom-gallery-container .gallery-item.hidden { 
      display: none; 
    }

    #custom-gallery-container .gallery-item img {
      width: 100%;
      height: auto;
      display: block;
      transition: transform 0.3s ease;
    }

    #custom-gallery-container .gallery-overlay {
      position: absolute;
      bottom: 0;
      left: 0;
      right: 0;
      background: linear-gradient(to top, rgba(0,0,0,0.85) 0%, rgba(0,0,0,0) 100%);
      color: #fff;
      padding: 40px 15px 15px 15px;
      opacity: 0;
      transform: translateY(10px);
      transition: all 0.3s ease;
      pointer-events: none;
      z-index: 2;
    }
    
    #custom-gallery-container .gallery-item:hover .gallery-overlay { 
      opacity: 1; 
      transform: translateY(0); 
    }
    
    #custom-gallery-container .gallery-item:hover img { 
      transform: scale(1.05); 
    }

    .overlay-title { 
      font-family: inherit; 
      font-size: 1rem; 
      font-weight: 600; 
      display: block; 
      margin-bottom: 4px; 
    }
    .overlay-desc { 
      font-family: inherit; 
      font-size: 0.8rem; 
      opacity: 0.9; 
      line-height: 1.3; 
    }
  </style>

  <div class="gallery-filters">
    <span class="filter-tag active" data-filter="all">all</span>
    <span class="filter-tag" data-filter="research">research</span>
    <span class="filter-tag" data-filter="moments">moments</span>
    <span class="filter-tag" data-filter="captures">captures</span>
  </div>

  <div class="gallery-grid" id="gallery-grid">
    <div class="gallery-item" data-category="research">
      <img src="{{ site.baseurl }}/assets/img/pi.jpg" alt="Who">
      <div class="gallery-overlay">
        <span class="overlay-title">Who</span>
        <span class="overlay-desc"> </span>
      </div>
    </div>
    <div class="gallery-item" data-category="moments">
      <img src="{{ site.baseurl }}/assets/img/darksister.jpeg" alt="Dark Sister">
      <div class="gallery-overlay">
        <span class="overlay-title">Dark Sister</span>
        <span class="overlay-desc">a longsword of Valyrian steel</span>
      </div>
    </div>
    <div class="gallery-item" data-category="moments">
      <img src="{{ site.baseurl }}/assets/img/dotd.png" alt="Dance of the Dragons">
      <div class="gallery-overlay">
        <span class="overlay-title">Dance of the Dragons</span>
        <span class="overlay-desc">The Dance over Shipbreaker Bay</span>
      </div>
    </div>
    <div class="gallery-item" data-category="research">
      <img src="{{ site.baseurl }}/assets/img/it.jpg" alt="Iron Throne">
      <div class="gallery-overlay">
        <span class="overlay-title">Iron Throne</span>
        <span class="overlay-desc">The throne of the monarchs of the Seven Kingdoms</span>
      </div>
    </div>
    <div class="gallery-item" data-category="moments">
      <img src="{{ site.baseurl }}/assets/img/the-conquest.jpg" alt="The Conquest">
      <div class="gallery-overlay">
        <span class="overlay-title">The Conquest</span>
        <span class="overlay-desc">Visenya Targaryen and Vhagar</span>
      </div>
    </div>
    <div class="gallery-item" data-category="captures">
      <img src="{{ site.baseurl }}/photos/pt/_YKM1194.jpg" alt="YKM1194">
      <div class="gallery-overlay">
        <span class="overlay-title"></span>
        <span class="overlay-desc"></span>
      </div>
    </div>
    <div class="gallery-item" data-category="captures">
      <img src="{{ site.baseurl }}/photos/pt/_YKM1216.jpg" alt="YKM1216">
      <div class="gallery-overlay">
        <span class="overlay-title"> </span>
        <span class="overlay-desc"> </span>
      </div>
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
