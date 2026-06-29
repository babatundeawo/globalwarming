/* Shared site behaviour: mobile menu, scroll-reveal, counting readouts */
(function(){
  "use strict";

  /* ---- mobile menu (slide-in drawer) ---- */
  var menuBtn = document.getElementById("menu-btn");
  var mobileMenu = document.getElementById("mobile-menu");
  var backdrop = document.getElementById("mobile-menu-backdrop");
  var closeBtn = document.getElementById("mobile-menu-close");

  function setMenu(open){
    if (!mobileMenu) return;
    mobileMenu.classList.toggle("is-open", open);
    if (backdrop) backdrop.classList.toggle("is-open", open);
    if (menuBtn){
      menuBtn.classList.toggle("is-open", open);
      menuBtn.setAttribute("aria-expanded", open ? "true" : "false");
    }
    document.body.style.overflow = open ? "hidden" : "";
  }

  if (menuBtn && mobileMenu){
    menuBtn.addEventListener("click", function(){
      setMenu(!mobileMenu.classList.contains("is-open"));
    });
    if (closeBtn) closeBtn.addEventListener("click", function(){ setMenu(false); });
    if (backdrop) backdrop.addEventListener("click", function(){ setMenu(false); });
    document.addEventListener("keydown", function(e){
      if (e.key === "Escape") setMenu(false);
    });
    mobileMenu.querySelectorAll("a").forEach(function(a){
      a.addEventListener("click", function(){ setMenu(false); });
    });
  }

  /* ---- scroll reveal ---- */
  var revealEls = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && revealEls.length){
    var io = new IntersectionObserver(function(entries){
      entries.forEach(function(entry){
        if (entry.isIntersecting){
          entry.target.classList.add("is-visible");
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12 });
    revealEls.forEach(function(el){ io.observe(el); });
  } else {
    revealEls.forEach(function(el){ el.classList.add("is-visible"); });
  }

  /* ---- animated readout counters ----
     usage: <span class="ro-value js-counter" data-target="427.3" data-decimals="1" data-suffix=""></span> */
  var counters = document.querySelectorAll(".js-counter");
  function animateCounter(el){
    var target = parseFloat(el.getAttribute("data-target") || "0");
    var decimals = parseInt(el.getAttribute("data-decimals") || "0", 10);
    var prefix = el.getAttribute("data-prefix") || "";
    var suffix = el.getAttribute("data-suffix") || "";
    var dur = 1100;
    var start = null;
    function step(ts){
      if (!start) start = ts;
      var p = Math.min(1, (ts - start) / dur);
      var eased = 1 - Math.pow(1 - p, 3);
      var val = target * eased;
      el.textContent = prefix + val.toFixed(decimals) + suffix;
      if (p < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }
  if (counters.length){
    if ("IntersectionObserver" in window){
      var cio = new IntersectionObserver(function(entries){
        entries.forEach(function(entry){
          if (entry.isIntersecting){
            animateCounter(entry.target);
            cio.unobserve(entry.target);
          }
        });
      }, { threshold: 0.4 });
      counters.forEach(function(el){ cio.observe(el); });
    } else {
      counters.forEach(animateCounter);
    }
  }

  /* ---- current year in footer ---- */
  var yearEl = document.querySelector(".js-year");
  if (yearEl) yearEl.textContent = new Date().getFullYear();

})();
