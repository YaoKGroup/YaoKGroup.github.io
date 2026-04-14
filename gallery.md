---
layout: page
title: "Gallery"
subtitle: "moments and memories"
permalink: /gallery/
---

<div id="custom-gallery-container">
  <style>
    #custom-gallery-container {
      font-family: "Source Serif 4", Georgia, "Times New Roman", Times, serif;
      color: #1b1f24;
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
      text-transform: none;
      cursor: pointer;
      color: var(--ust-blue);
      padding: 5px 0;
      transition: all 0.3s ease;
      position: relative;
    }

    #custom-gallery-container .filter-tag:hover { color: var(--gold-hover); }
    #custom-gallery-container .filter-tag.active { font-weight: bold; color: var(--gold); }
    #custom-gallery-container .filter-tag.active::after {
      content: '';
      position: absolute;
      bottom: -16px;
      left: 0;
      width: 100%;
      height: 3px;
      background: #996600;
    }

    /* Masonry */
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
      position: relative;
      border-radius: 10px;
      overflow: hidden;
      background: #f9f9f9;
      transition: opacity 0.4s ease, transform 0.4s ease;
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

    .overlay-title { font-family: inherit; font-size: 1rem; font-weight: 600; display: block; margin-bottom: 4px; }
    .overlay-desc { font-family: inherit; font-size: 0.8rem; opacity: 0.9; line-height: 1.3; }
  </style>

  <div class="gallery-filters">
    <span class="filter-tag active" data-filter="all">All</span>
    <span class="filter-tag" data-filter="research">Research</span>
    <span class="filter-tag" data-filter="activities">Activities</span>
    <span class="filter-tag" data-filter="memories">Memories</span>
  </div>

  <div class="gallery-grid" id="gallery-grid">
    
    <div class="gallery-item" data-category="research">
      <img src="{{ site.baseurl }}/assets/img/pi.jpg" alt="Research 1">
      <div class="gallery-overlay">
        <span class="overlay-title">Field Study</span>
        <span class="overlay-desc">Experimental data collection and analysis.</span>
      </div>
    </div>
    <div class="gallery-item" data-category="research">
      <img src="{{ site.baseurl }}/assets/img/dotd.png" alt="Research 2">
      <div class="gallery-overlay">
        <span class="overlay-title">Numerical Simulation</span>
        <span class="overlay-desc">Modeling complex flow structures.</span>
      </div>
    </div>

    <div class="gallery-item" data-category="activities">
      <img src="{{ site.baseurl }}/assets/img/the-conquest.jpg" alt="Activities 1">
      <div class="gallery-overlay">
        <span class="overlay-title">Conference Talk</span>
        <span class="overlay-desc">Presenting latest findings at the symposium.</span>
      </div>
    </div>
    <div class="gallery-item" data-category="activities">
      <img src="{{ site.baseurl }}/assets/img/it.jpg" alt="Activities 2">
      <div class="gallery-overlay">
        <span class="overlay-title">Lab Discussion</span>
        <span class="overlay-desc">Weekly brainstorming session in the meeting room.</span>
      </div>
    </div>

    <div class="gallery-item" data-category="memories">
      <img src="{{ site.baseurl }}/assets/img/darksister.jpeg" alt="Memories 1">
      <div class="gallery-overlay">
        <span class="overlay-title">Campus Life</span>
        <span class="overlay-desc">Beautiful scenery during the autumn semester.</span>
      </div>
    </div>
    <div class="gallery-item" data-category="memories">
      <img src="{{ site.baseurl }}/assets/img/placeholder-member.jpg" alt="Memories 2">
      <div class="gallery-overlay">
        <span class="overlay-title">Group Dinner</span>
        <span class="overlay-desc">Celebrating the successful project completion.</span>
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
