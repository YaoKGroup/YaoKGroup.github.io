---
layout: page
title: "研究方向"
subtitle: ""
permalink: /zh/research/
lang: zh
en_url: /research/
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
      <div class="cover-wrapper"><img src="{{ '/photos/art/nmi2022.webp' | relative_url }}" class="cover-img" alt="Journal 1"></div>
      <div class="cover-wrapper"><img src="{{ '/photos/art/jmca2022.webp' | relative_url }}" class="cover-img" alt="Journal 2"></div>
      <div class="cover-wrapper"><img src="{{ '/photos/art/csr2024.jpg' | relative_url }}" class="cover-img" alt="Journal 3"></div>
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

<h2>可穿戴触觉交互界面</h2>

<div class="two-col">
  <div class="two-col-media">
    <div class="research-carousel" data-carousel="wearable-haptics">
      <div class="research-carousel-track">
        <div class="research-carousel-slide">
          <img src="{{ '/photos/research/hpt1.png' | relative_url }}" alt="可穿戴触觉交互界面 1">
        </div>
        <div class="research-carousel-slide">
          <img src="{{ '/photos/research/hpt2.png' | relative_url }}" alt="可穿戴触觉交互界面 2">
        </div>
        <div class="research-carousel-slide">
          <img src="{{ '/photos/research/hpt3.png' | relative_url }}" alt="可穿戴触觉交互界面 3">
        </div>
      </div>

      <a class="carousel-control-prev research-carousel-prev" href="javascript:void(0)" aria-label="上一张图片">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      </a>
      <a class="carousel-control-next research-carousel-next" href="javascript:void(0)" aria-label="下一张图片">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
      </a>
    </div>
  </div>

  <div class="two-col-text">
    <p>
      我们开发用于虚拟现实和增强现实的触觉交互界面，让用户在虚拟世界中感受到真实触碰。不同于传统商用设备，我们的器件不再厚重笨拙，也不会给使用者带来明显负担或束缚；它们可以被设计成柔软、轻薄、可穿戴且不影响日常交互。结合低功耗蓝牙（BLE）等无线通信技术，触觉刺激可以通过手机端按钮在手部任意位置触发，也可以与虚拟现实场景中的碰撞事件同步。未来，我们将继续通过先进材料和系统集成策略提升界面的舒适性和沉浸感。
    </p>
  </div>
</div>

<h2>植入式生物电子器件</h2>

<div class="two-col">
  <div class="two-col-media">
    <div class="research-carousel" data-carousel="implantable-bioelectronics">
      <div class="research-carousel-track">
        <div class="research-carousel-slide">
          <img src="{{ '/photos/research/bio1.png' | relative_url }}" alt="植入式生物电子器件 1">
        </div>
      </div>

      <a class="carousel-control-prev research-carousel-prev" href="javascript:void(0)" aria-label="上一张图片">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      </a>
      <a class="carousel-control-next research-carousel-next" href="javascript:void(0)" aria-label="下一张图片">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
      </a>
    </div>
  </div>

  <div class="two-col-text">
    <p>
      我们致力于开发面向多种生物医学应用的先进植入式生物电子器件，例如电生理信号监测（如 ECoG、EMG、EKG 等）、用于肌肉康复的电刺激、药物递送以及神经调控（如光遗传学、深脑刺激 DBS、迷走神经刺激 VNS 等）。这类植入器件需要具备良好的生物相容性，避免对生物组织造成损伤；它们可以足够稳定以支持长期使用，也可以设计成暂态可降解系统，在完成任务后被人体吸收，从而避免二次手术取出。
    </p>
  </div>
</div>

<h2>先进制造：柔性、可透气三维电子系统</h2>

<div class="two-col">
  <div class="two-col-media">
    <div class="research-carousel" data-carousel="advanced-manufacturing">
      <div class="research-carousel-track">
        <div class="research-carousel-slide">
          <img src="{{ '/photos/research/es1.png' | relative_url }}" alt="电子系统 1">
        </div>
        <div class="research-carousel-slide">
          <img src="{{ '/photos/research/es2.png' | relative_url }}" alt="电子系统 2">
        </div>
      </div>

      <a class="carousel-control-prev research-carousel-prev" href="javascript:void(0)" aria-label="上一张图片">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      </a>
      <a class="carousel-control-next research-carousel-next" href="javascript:void(0)" aria-label="下一张图片">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
      </a>
    </div>
  </div>

  <div class="two-col-text">
    <p>
      多数可拉伸电子系统集成密度较低，并依赖外接印刷电路板布线，这会限制系统功能、降低用户体验，并影响长期使用。我们关注本征可透气的三维集成电子皮肤，通过三维图案化、多层液态金属电路和可拉伸混合液态金属焊料，将高密度无机电子元件与有机可拉伸纤维基底集成在一起。该电子皮肤兼具高柔软性、耐久性、类似织物的透气透湿能力，以及可支持一周皮肤贴附的生物相容性。
    </p>
  </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  /*
    Top journal carousel:
    - 1 to 5 images: show from the left, keep empty space on the right, no movement.
    - More than 5 images: enable arrows and autoplay.
  */
  const wrapper = document.querySelector('.cards-wrapper');
  const nextBtn = document.querySelector('#journalCarousel .carousel-control-next');
  const prevBtn = document.querySelector('#journalCarousel .carousel-control-prev');
  const journalCarousel = document.querySelector('#journalCarousel');

  if (wrapper && nextBtn && prevBtn && journalCarousel) {
    let isTransitioning = false;
    const visibleCount = 5;
    const totalItems = wrapper.children.length;
    const itemWidth = 100 / visibleCount;
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

        setTimeout(function() {
          isTransitioning = false;
        }, 50);

        wrapper.removeEventListener('transitionend', handleEnd);
      });
    }

    function showPrev() {
      if (isTransitioning) return;

      isTransitioning = true;
      wrapper.style.transition = 'none';
      wrapper.prepend(wrapper.lastElementChild);
      wrapper.style.transform = `translateX(-${itemWidth}%)`;

      setTimeout(function() {
        wrapper.style.transition = 'transform 0.5s ease-in-out';
        wrapper.style.transform = 'translateX(0)';
      }, 10);

      wrapper.addEventListener('transitionend', function() {
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

    if (totalItems <= visibleCount) {
      wrapper.style.transition = 'none';
      wrapper.style.transform = 'translateX(0)';
      prevBtn.style.display = 'none';
      nextBtn.style.display = 'none';
    } else {
      prevBtn.style.display = '';
      nextBtn.style.display = '';

      nextBtn.addEventListener('click', function(e) {
        e.preventDefault();
        showNext();
        startAutoPlay();
      });

      prevBtn.addEventListener('click', function(e) {
        e.preventDefault();
        showPrev();
        startAutoPlay();
      });

      journalCarousel.addEventListener('mouseenter', stopAutoPlay);
      journalCarousel.addEventListener('mouseleave', startAutoPlay);

      startAutoPlay();
    }
  }

  /*
    Research section carousels:
    - 1 image: hide arrows.
    - 2 or more images: show arrows and switch images.
  */
  document.querySelectorAll('.research-carousel').forEach(function(carouselEl) {
    const track = carouselEl.querySelector('.research-carousel-track');
    const prev = carouselEl.querySelector('.research-carousel-prev');
    const next = carouselEl.querySelector('.research-carousel-next');

    if (!track || !prev || !next) return;

    const originalSlides = Array.from(track.children);
    const total = originalSlides.length;

    if (total <= 1) {
      prev.style.display = 'none';
      next.style.display = 'none';
      return;
    }

    prev.style.display = '';
    next.style.display = '';

    const firstClone = originalSlides[0].cloneNode(true);
    const lastClone = originalSlides[total - 1].cloneNode(true);

    track.appendChild(firstClone);
    track.insertBefore(lastClone, track.firstChild);

    let index = 1;
    let locked = false;

    track.style.transition = 'none';
    track.style.transform = `translateX(-${index * 100}%)`;

    function moveToCurrentIndex(withAnimation) {
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

      setTimeout(function() {
        locked = false;
      }, 20);
    });

    waitForImagesAndSetHeight();
    window.addEventListener('resize', setCarouselHeight);
  });
});
</script>
