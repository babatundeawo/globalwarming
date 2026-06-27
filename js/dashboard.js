/* Class Dashboard — fetches roster-data.json (built by the GitHub Action)
   and renders it. Handles the "no data yet" first-run state gracefully. */
(function(){
  "use strict";
  var mount = document.getElementById("dashboard-mount");
  if (!mount) return;

  function escapeHtml(s){
    return String(s == null ? "" : s).replace(/[&<>"']/g, function(c){
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", "\"": "&quot;", "'": "&#39;" }[c];
    });
  }

  function timeAgo(iso){
    if (!iso) return "";
    var d = new Date(iso);
    if (isNaN(d.getTime())) return "";
    var diff = Math.max(0, Date.now() - d.getTime());
    var mins = Math.floor(diff / 60000);
    if (mins < 1) return "just now";
    if (mins < 60) return mins + "m ago";
    var hrs = Math.floor(mins / 60);
    if (hrs < 24) return hrs + "h ago";
    var days = Math.floor(hrs / 24);
    return days + "d ago";
  }

  function stat(value, label){
    return '<div class="fact"><div class="fv">' + value + '</div><div class="fl">' + label + '</div></div>';
  }

  function renderEmpty(){
    mount.innerHTML =
      '<div class="callout callout--note">' +
      '<span class="callout-label">No check-ins yet</span>' +
      '<p>This page reads <code>roster-data.json</code>, which a free GitHub Action regenerates automatically whenever someone submits the <a href="checkin.html">Check In</a> form. Once the first check-in Issue lands in the repo, this dashboard fills in on its own — usually within minutes, or up to a few hours on the scheduled fallback run.</p>' +
      '<p style="margin-top:10px;">Site owner: if this message persists after a real check-in, open the repo\u2019s <strong>Actions</strong> tab and confirm the "Update Class Dashboard" workflow ran successfully.</p>' +
      '</div>';
  }

  function renderError(){
    mount.innerHTML =
      '<div class="callout callout--note"><span class="callout-label">Dashboard data not found yet</span>' +
      '<p>That\u2019s expected before the first check-in or the first Action run. See the note above for what happens next.</p></div>';
  }

  function render(data){
    var students = data.students || [];
    var checkins = data.checkins || [];
    if (!students.length){ renderEmpty(); return; }

    var avg = students.reduce(function(s, x){ return s + (x.progress || 0); }, 0) / students.length;
    var finished = students.filter(function(s){ return s.progress >= 8; }).length;

    var html = '<div class="grid grid-4 reveal" style="margin-bottom:10px;">' +
      stat(data.total_students || students.length, "Students checked in") +
      stat(data.total_checkins || checkins.length, "Total check-ins") +
      stat(avg.toFixed(1), "Avg. lessons / student") +
      stat(finished, "Finished all 8") +
      '</div>';

    html += '<p class="muted" style="font-size:.8rem;margin:0 0 20px;">Last updated ' +
      escapeHtml(timeAgo(data.generated_at) || "recently") + ' · refreshes automatically</p>';

    html += '<ol class="lesson-list reveal">';
    students.forEach(function(s){
      var pct = Math.round(((s.progress || 0) / 8) * 100);
      var done = (s.progress || 0) >= 8;
      html += '<li class="lesson-card' + (done ? " is-complete" : "") + '" style="cursor:default;">' +
        '<span class="ln">' + (s.progress != null ? s.progress : "?") + '</span>' +
        '<div style="flex:1;min-width:0;">' +
          '<div class="lc-title">' + escapeHtml(s.name) + '</div>' +
          '<div class="lc-obj">' + (s.progress || 0) + ' of 8 lessons &middot; last check-in ' + escapeHtml(timeAgo(s.updated_at || s.created_at) || "recently") + '</div>' +
          '<div class="result-bar" style="margin-top:8px;height:8px;background:var(--line-soft);"><span style="width:' + pct + '%;"></span></div>' +
        '</div>' +
        (s.issue_url ? '<a class="lesson-check" href="' + s.issue_url + '" target="_blank" rel="noopener">Issue →</a>' : "") +
        '</li>';
    });
    html += '</ol>';

    mount.innerHTML = html;
  }

  fetch("roster-data.json", { cache: "no-store" })
    .then(function(r){ if (!r.ok) throw new Error("not found"); return r.json(); })
    .then(render)
    .catch(renderError);
})();
