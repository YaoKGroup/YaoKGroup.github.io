---
layout: page
title: "Research"
subtitle: "research subtitle"
permalink: /research/
---

<style>
  .two-col {
    display: flex;
    gap: 2rem;
    align-items: flex-start;
    margin-bottom: 2.5rem;
  }

  .two-col-media {
    flex: 0 0 42%;
  }

  .two-col-text {
    flex: 1 1 auto;
  }

  .two-col-media img {
    width: 100%;
    height: auto;
    display: block;
    border-radius: 8px;
  }

  .research-carousel {
    position: relative;
    overflow: hidden;
    width: 100%;
    border-radius: 8px;
  }

  .research-carousel-track {
    display: flex;
    will-change: transform;
  }

  .research-carousel-slide {
    min-width: 100%;
    flex: 0 0 100%;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .research-carousel-slide img {
    width: 100%;
    height: auto;
    display: block;
    border-radius: 8px;
  }

  .research-carousel .research-carousel-prev,
  .research-carousel .research-carousel-next {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    z-index: 2;
    width: 15%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    text-decoration: none;
    background: none;
    border: none;
    box-shadow: none;
    opacity: 1;
    transition: transform 0.2s ease;
  }

  .research-carousel .research-carousel-prev {
    left: 0;
  }

  .research-carousel .research-carousel-next {
    right: 0;
  }

  .research-carousel .carousel-control-prev-icon,
  .research-carousel .carousel-control-next-icon {
    opacity: 0.85;
    transition: transform 0.2s ease, opacity 0.2s ease;
  }

  .research-carousel .research-carousel-prev:hover,
  .research-carousel .research-carousel-next:hover {
    transform: translateY(-50%) scale(1.08);
  }

  .research-carousel .research-carousel-prev:hover .carousel-control-prev-icon,
  .research-carousel .research-carousel-next:hover .carousel-control-next-icon {
    opacity: 0.85;
  }

  @media (max-width: 768px) {
    .two-col {
      flex-direction: column;
    }

    .two-col-media,
    .two-col-text {
      flex: 1 1 100%;
      width: 100%;
    }
  }
</style>

<div id="journalCarousel" class="carousel slide journal-carousel">
  <div class="carousel-inner">
    <div class="cards-wrapper">
      <div class="cover-wrapper"><img src="{{ '/assets/img/darksister.jpeg' | relative_url }}" class="cover-img" alt="Journal 1"></div>
      <div class="cover-wrapper"><img src="{{ '/assets/img/darksister.jpeg' | relative_url }}" class="cover-img" alt="Journal 2"></div>
      <div class="cover-wrapper"><img src="{{ '/assets/img/darksister.jpeg' | relative_url }}" class="cover-img" alt="Journal 3"></div>
      <div class="cover-wrapper"><img src="{{ '/assets/img/darksister.jpeg' | relative_url }}" class="cover-img" alt="Journal 4"></div>
      <div class="cover-wrapper"><img src="{{ '/assets/img/darksister.jpeg' | relative_url }}" class="cover-img" alt="Journal 5"></div>
      <div class="cover-wrapper"><img src="{{ '/assets/img/darksister.jpeg' | relative_url }}" class="cover-img" alt="Journal 6"></div>
      <div class="cover-wrapper"><img src="{{ '/assets/img/darksister.jpeg' | relative_url }}" class="cover-img" alt="Journal 7"></div>
      <div class="cover-wrapper"><img src="{{ '/assets/img/darksister.jpeg' | relative_url }}" class="cover-img" alt="Journal 8"></div>
    </div>
  </div>

  <a class="carousel-control-prev" href="javascript:void(0)" role="button">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
  </a>
  <a class="carousel-control-next" href="javascript:void(0)" role="button">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
  </a>
</div>

<hr>

<h2>Wearable haptic interfaces</h2>

<div class="two-col">
  <div class="two-col-media">
    <div class="research-carousel" data-carousel="wearable-haptics">
      <div class="research-carousel-track">
        <div class="research-carousel-slide">
          <img src="{{ '/assets/img/the-conquest.jpg' | relative_url }}" alt="Wearable haptic interfaces 1">
        </div>
        <div class="research-carousel-slide">
          <img src="{{ '/assets/img/it.jpg' | relative_url }}" alt="Wearable haptic interfaces 2">
        </div>
        <div class="research-carousel-slide">
          <img src="{{ '/assets/img/the-conquest.jpg' | relative_url }}" alt="Wearable haptic interfaces 3">
        </div>
      </div>

      <a class="carousel-control-prev research-carousel-prev" href="javascript:void(0)" aria-label="Previous image">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      </a>
      <a class="carousel-control-next research-carousel-next" href="javascript:void(0)" aria-label="Next image">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
      </a>
    </div>
  </div>

  <div class="two-col-text">
    <p>
      We develop haptic interfaces that help VR and AR users to feel the touch in the virtual world. Unlike commercial ones, our devices are no longer heavy or bulky, making users feel loaded or restricted. Instead, they can be made soft, thin, light-weighted, wearable and unobtrusive when using. Using wireless communication techs like Bluetooth Low Energy (BLE), stimulation could be triggered on anywhere of the hand by simply clicking a button on the mobile phone, or just be synchronized with the VR when collisions detected. In the future, we keep trying to make the interface more comfortable by using advanced materials and system integration strategies.
    </p>
  </div>
</div>

<h2>Implantable bioelectronics</h2>

<div class="two-col">
  <div class="two-col-media">
    <div class="research-carousel" data-carousel="implantable-bioelectronics">
      <div class="research-carousel-track">
        <div class="research-carousel-slide">
          <img src="{{ '/assets/img/dotd.png' | relative_url }}" alt="Implantable bioelectronics 1">
        </div>
        <div class="research-carousel-slide">
          <img src="{{ '/assets/img/dotd.png' | relative_url }}" alt="Implantable bioelectronics 2">
        </div>
      </div>

      <a class="carousel-control-prev research-carousel-prev" href="javascript:void(0)" aria-label="Previous image">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      </a>
      <a class="carousel-control-next research-carousel-next" href="javascript:void(0)" aria-label="Next image">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
      </a>
    </div>
  </div>

  <div class="two-col-text">
    <p>
      We make efforts to develop advanced implantable bioelectronics for multi-purpose biomedical applications, such as electrophysiological signal monitoring (e.g. ECoG, EMG, EKG, etc.), electrostimulation for muscle rehabilitation, drug delivery, and neuromodulations (e.g. optogenetics, deep brain stimulations (DBS), vagus nerve stimulations (VNS), etc.). These implantables should be biocompatible that won't cause damage to the biological tissue, and will either be stable enough for long-term use or be transient that could be degraded by the body once it's not needed anymore, to avoid second-time surgery to take them out.
    </p>
  </div>
</div>

<h2>Advanced manufacturing: soft, permeable 3D electronic system</h2>

<div class="two-col">
  <div class="two-col-media">
    <div class="research-carousel" data-carousel="advanced-manufacturing">
      <div class="research-carousel-track">
        <div class="research-carousel-slide">
          <img src="{{ '/assets/img/the-conquest.jpg' | relative_url }}" alt="Advanced manufacturing 1">
        </div>
      </div>

      <a class="carousel-control-prev research-carousel-prev" href="javascript:void(0)" aria-label="Previous image">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      </a>
      <a class="carousel-control-next research-carousel-next" href="javascript:void(0)" aria-label="Next image">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
      </a>
    </div>
  </div>

  <div class="two-col-text">
    <p>
      Most stretchable electronic systems have low-density integration and are wired with external printed circuit boards, which limits functionality, deteriorates user experience and impedes long-term usability. Here we report an intrinsically permeable, three-dimensional integrated electronic skin. The system combines high-density inorganic electronic components with organic stretchable fibrous substrates using three-dimensional patterned, multilayered liquid metal circuits and stretchable hybrid liquid metal solder. The electronic skin exhibits high softness, durability, fabric-like permeability to air and moisture and sufficient biocompatibility for on-skin attachment for a week.
    </p>
  </div>
</div>

<h2>Projects</h2>
<ul>
  <li>Project A</li>
  <li>Project B</li>
</ul>

<script>
document.addEventListener('DOMContentLoaded', function() {
  const wrapper = document.querySelector('.cards-wrapper');
  const nextBtn = document.querySelector('#journalCarousel .carousel-control-next');
  const prevBtn = document.querySelector('#journalCarousel .carousel-control-prev');
  const carousel = document.querySelector('#journalCarousel');

  let isTransitioning = false;
  const itemWidth = 20;
  let autoPlayTimer = null;

  function showNext() {
    if (isTransitioning) return;
    isTransitioning = true;
    wrapper.style.transition = 'transform 0.5s ease-in-out';
    wrapper.style.transform = `translateX(-${itemWidth}%)`;

    wrapper.addEventListener('transitionend', function handleEnd() {
      wrapper.style.transition = 'none';
      wrapper.appendChild(wrapper.firstElementChild);
      wrapper.style.transform = 'translateX(0)';
      setTimeout(() => { isTransitioning = false; }, 50);
      wrapper.removeEventListener('transitionend', handleEnd);
    });
  }

  function showPrev() {
    if (isTransitioning) return;
    isTransitioning = true;
    wrapper.style.transition = 'none';
    wrapper.prepend(wrapper.lastElementChild);
    wrapper.style.transform = `translateX(-${itemWidth}%)`;
    setTimeout(() => {
      wrapper.style.transition = 'transform 0.5s ease-in-out';
      wrapper.style.transform = 'translateX(0)';
    }, 10);
    wrapper.addEventListener('transitionend', () => {
      isTransitioning = false;
    }, { once: true });
  }

  function stopAutoPlay() {
    if (autoPlayTimer) {
      clearInterval(autoPlayTimer);
      autoPlayTimer = null;
    }
  }

  function startAutoPlay() {
    stopAutoPlay();
    autoPlayTimer = setInterval(showNext, 3000);
  }

  nextBtn.addEventListener('click', (e) => {
    e.preventDefault();
    showNext();
    startAutoPlay();
  });

  prevBtn.addEventListener('click', (e) => {
    e.preventDefault();
    showPrev();
    startAutoPlay();
  });

  carousel.addEventListener('mouseenter', stopAutoPlay);
  carousel.addEventListener('mouseleave', startAutoPlay);

  startAutoPlay();

  document.querySelectorAll('.research-carousel').forEach(function(carouselEl) {
    const track = carouselEl.querySelector('.research-carousel-track');
    const prev = carouselEl.querySelector('.research-carousel-prev');
    const next = carouselEl.querySelector('.research-carousel-next');

    const originalSlides = Array.from(track.children);
    const total = originalSlides.length;

    if (total <= 1) {
      if (prev) prev.style.display = 'none';
      if (next) next.style.display = 'none';
      return;
    }

    const firstClone = originalSlides[0].cloneNode(true);
    const lastClone = originalSlides[total - 1].cloneNode(true);

    track.appendChild(firstClone);
    track.insertBefore(lastClone, track.firstChild);

    let index = 1;
    let locked = false;

    track.style.transition = 'none';
    track.style.transform = `translateX(-${index * 100}%)`;

    function moveToCurrentIndex(withAnimation = true) {
      track.style.transition = withAnimation ? 'transform 0.5s ease-in-out' : 'none';
      track.style.transform = `translateX(-${index * 100}%)`;
    }

    function setCarouselHeight() {
      const images = carouselEl.querySelectorAll('.research-carousel-slide img');
      let maxHeight = 0;

      images.forEach(function(img) {
        if (img.offsetHeight > maxHeight) {
          maxHeight = img.offsetHeight;
        }
      });

      if (maxHeight > 0) {
        carouselEl.style.height = maxHeight + 'px';
        carouselEl.querySelectorAll('.research-carousel-slide').forEach(function(slide) {
          slide.style.height = maxHeight + 'px';
        });
      }
    }

    function waitForImagesAndSetHeight() {
      const images = carouselEl.querySelectorAll('.research-carousel-slide img');
      let loadedCount = 0;

      function done() {
        loadedCount += 1;
        if (loadedCount === images.length) {
          setCarouselHeight();
        }
      }

      images.forEach(function(img) {
        if (img.complete) {
          done();
        } else {
          img.addEventListener('load', done, { once: true });
          img.addEventListener('error', done, { once: true });
        }
      });
    }

    next.addEventListener('click', function(e) {
      e.preventDefault();
      if (locked) return;
      locked = true;
      index += 1;
      moveToCurrentIndex(true);
    });

    prev.addEventListener('click', function(e) {
      e.preventDefault();
      if (locked) return;
      locked = true;
      index -= 1;
      moveToCurrentIndex(true);
    });

    track.addEventListener('transitionend', function() {
      if (index === total + 1) {
        index = 1;
        moveToCurrentIndex(false);
      } else if (index === 0) {
        index = total;
        moveToCurrentIndex(false);
      }

      setTimeout(() => {
        locked = false;
      }, 20);
    });

    waitForImagesAndSetHeight();
    window.addEventListener('resize', setCarouselHeight);
  });
});
</script>
