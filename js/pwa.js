/* Install, update, share and iOS "Add to Home Screen" behaviour.
   Loaded on every page. No inline scripts, so the Content Security Policy stays strict. */
(function () {
  "use strict";

  var DISMISS_KEY = "gw-install-dismissed";
  var IOS_KEY = "gw-ios-dismissed";

  function store(get, key, val) {
    try { return get ? localStorage.getItem(key) : localStorage.setItem(key, val); } catch (e) { return null; }
  }
  function byId(id) { return document.getElementById(id); }
  function isStandalone() {
    return (window.matchMedia && window.matchMedia("(display-mode: standalone)").matches) || window.navigator.standalone === true;
  }

  /* ---- service worker + safe update flow ---- */
  var updateToast = byId("update-toast");
  var updateBtn = byId("update-accept");
  var updateLater = byId("update-dismiss");
  var waitingWorker = null;
  var reloading = false;

  function showUpdate(worker) {
    waitingWorker = worker;
    if (updateToast) updateToast.classList.add("is-open");
  }

  if ("serviceWorker" in navigator) {
    window.addEventListener("load", function () {
      navigator.serviceWorker.register("sw.js").then(function (reg) {
        if (reg.waiting && navigator.serviceWorker.controller) showUpdate(reg.waiting);
        reg.addEventListener("updatefound", function () {
          var nw = reg.installing;
          if (!nw) return;
          nw.addEventListener("statechange", function () {
            if (nw.state === "installed" && navigator.serviceWorker.controller) showUpdate(nw);
          });
        });
      }).catch(function () {});
    });
    navigator.serviceWorker.addEventListener("controllerchange", function () {
      if (reloading) return;
      reloading = true;
      window.location.reload();
    });
  }
  if (updateBtn) updateBtn.addEventListener("click", function () {
    if (waitingWorker) waitingWorker.postMessage({ type: "SKIP_WAITING" });
    else window.location.reload();
  });
  if (updateLater) updateLater.addEventListener("click", function () {
    if (updateToast) updateToast.classList.remove("is-open");
  });

  /* ---- install prompt (Chrome, Edge, Android) ---- */
  var installToast = byId("install-toast");
  var deferred = null;
  window.addEventListener("beforeinstallprompt", function (e) {
    e.preventDefault();
    deferred = e;
    if (store(true, DISMISS_KEY) === "1" || isStandalone()) return;
    setTimeout(function () { if (installToast && deferred) installToast.classList.add("is-open"); }, 12000);
  });
  var accept = byId("install-accept");
  var dismiss = byId("install-dismiss");
  if (accept) accept.addEventListener("click", function () {
    if (installToast) installToast.classList.remove("is-open");
    if (deferred) { deferred.prompt(); deferred = null; }
  });
  if (dismiss) dismiss.addEventListener("click", function () {
    if (installToast) installToast.classList.remove("is-open");
    store(false, DISMISS_KEY, "1");
  });
  window.addEventListener("appinstalled", function () {
    if (installToast) installToast.classList.remove("is-open");
  });

  /* ---- iOS Safari: no install event exists, so show a short guide ---- */
  var ua = navigator.userAgent || "";
  var isIOS = /iphone|ipad|ipod/i.test(ua) || (navigator.platform === "MacIntel" && navigator.maxTouchPoints > 1);
  var isSafari = /safari/i.test(ua) && !/crios|fxios|edgios|opios/i.test(ua);
  var iosToast = byId("ios-toast");
  if (iosToast && isIOS && isSafari && !isStandalone() && store(true, IOS_KEY) !== "1") {
    setTimeout(function () { iosToast.classList.add("is-open"); }, 20000);
  }
  var iosClose = byId("ios-dismiss");
  if (iosClose) iosClose.addEventListener("click", function () {
    if (iosToast) iosToast.classList.remove("is-open");
    store(false, IOS_KEY, "1");
  });

  /* ---- Web Share button (only where the browser supports it) ---- */
  var shareBtn = byId("share-btn");
  if (shareBtn && navigator.share) {
    shareBtn.hidden = false;
    shareBtn.addEventListener("click", function () {
      navigator.share({ title: document.title, url: window.location.href }).catch(function () {});
    });
  }

  /* ---- print buttons (replaces inline onclick, which the CSP forbids) ---- */
  document.addEventListener("click", function (e) {
    var t = e.target.closest ? e.target.closest("[data-print]") : null;
    if (t) window.print();
  });

  /* ---- image fallback (replaces inline onerror, which the CSP forbids) ---- */
  function showFallback(img) {
    img.style.display = "none";
    if (img.nextElementSibling) img.nextElementSibling.style.display = "flex";
  }
  document.querySelectorAll("img[data-fallback]").forEach(function (img) {
    if (img.complete && img.naturalWidth === 0) showFallback(img);
    else img.addEventListener("error", function () { showFallback(img); });
  });

  /* ---- honest offline indicator ---- */
  var offline = byId("offline-badge");
  function syncOnline() { if (offline) offline.hidden = navigator.onLine; }
  window.addEventListener("online", syncOnline);
  window.addEventListener("offline", syncOnline);
  syncOnline();
})();
