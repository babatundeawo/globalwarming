/* Certificate of Completion — drawn on canvas, downloadable as PNG */
(function(){
  "use strict";
  var canvas = document.getElementById("cert-canvas");
  if (!canvas) return;
  var ctx = canvas.getContext("2d");
  var nameInput = document.getElementById("cert-name");
  var downloadBtn = document.getElementById("cert-download");

  var W = 1000, H = 700;
  canvas.width = W; canvas.height = H;

  function todayStr(){
    var d = new Date();
    var months = ["January","February","March","April","May","June","July","August","September","October","November","December"];
    return months[d.getMonth()] + " " + d.getDate() + ", " + d.getFullYear();
  }

  function draw(name){
    name = (name || "").trim() || "Your Name Here";

    ctx.fillStyle = "#FFFFFF";
    ctx.fillRect(0, 0, W, H);

    // outer border
    ctx.strokeStyle = "#0E5C56";
    ctx.lineWidth = 10;
    ctx.strokeRect(20, 20, W - 40, H - 40);
    ctx.strokeStyle = "#EE8C3C";
    ctx.lineWidth = 3;
    ctx.strokeRect(38, 38, W - 76, H - 76);

    // corner isoline-style flourish (simple arcs, echoes site motif)
    ctx.strokeStyle = "rgba(14,92,86,0.25)";
    ctx.lineWidth = 2;
    for (var i = 0; i < 4; i++){
      ctx.beginPath();
      ctx.arc(70, 70, 26 + i * 10, Math.PI, 1.5 * Math.PI);
      ctx.stroke();
      ctx.beginPath();
      ctx.arc(W - 70, H - 70, 26 + i * 10, 0, 0.5 * Math.PI);
      ctx.stroke();
    }

    ctx.textAlign = "center";

    ctx.fillStyle = "#D9691A";
    ctx.font = "700 16px 'JetBrains Mono', monospace";
    ctx.fillText("GLOBAL WARMING EXPLORER · GUIDED COURSE", W / 2, 110);

    ctx.fillStyle = "#11201C";
    ctx.font = "700 46px 'Space Grotesk', sans-serif";
    ctx.fillText("Certificate of Completion", W / 2, 170);

    ctx.fillStyle = "#45564E";
    ctx.font = "400 18px 'Plus Jakarta Sans', sans-serif";
    ctx.fillText("This certifies that", W / 2, 250);

    ctx.fillStyle = "#0A4641";
    ctx.font = "700 44px 'Space Grotesk', sans-serif";
    // shrink font if the name is long
    var fontSize = 44;
    ctx.font = fontSize + "px 'Space Grotesk', sans-serif";
    while (ctx.measureText(name).width > W - 200 && fontSize > 22){
      fontSize -= 2;
      ctx.font = "700 " + fontSize + "px 'Space Grotesk', sans-serif";
    }
    ctx.fillText(name, W / 2, 320);

    ctx.strokeStyle = "#CBD8CD";
    ctx.beginPath();
    ctx.moveTo(W / 2 - 220, 340);
    ctx.lineTo(W / 2 + 220, 340);
    ctx.stroke();

    ctx.fillStyle = "#45564E";
    ctx.font = "400 18px 'Plus Jakarta Sans', sans-serif";
    wrapText("has successfully completed all eight lessons of the Global Warming Explorer guided course, covering the science, effects, and real actions behind a warming world.", W / 2, 380, 620, 26);

    ctx.fillStyle = "#6E7D75";
    ctx.font = "400 15px 'JetBrains Mono', monospace";
    ctx.fillText(todayStr(), W / 2, 480);

    // signature block
    ctx.strokeStyle = "#CBD8CD";
    ctx.beginPath();
    ctx.moveTo(W / 2 - 160, 560);
    ctx.lineTo(W / 2 + 160, 560);
    ctx.stroke();
    ctx.fillStyle = "#11201C";
    ctx.font = "700 17px 'Space Grotesk', sans-serif";
    ctx.fillText("Babatunde Ayoola Awoyemi", W / 2, 585);
    ctx.fillStyle = "#6E7D75";
    ctx.font = "400 14px 'Plus Jakarta Sans', sans-serif";
    ctx.fillText("Techbase Consultant Services · Global Warming Explorer", W / 2, 606);

    ctx.textAlign = "left";
  }

  function wrapText(text, cx, y, maxWidth, lineHeight){
    var words = text.split(" ");
    var line = "";
    var lines = [];
    for (var i = 0; i < words.length; i++){
      var test = line + words[i] + " ";
      if (ctx.measureText(test).width > maxWidth && line){
        lines.push(line);
        line = words[i] + " ";
      } else {
        line = test;
      }
    }
    lines.push(line);
    lines.forEach(function(l, idx){
      ctx.fillText(l.trim(), cx, y + idx * lineHeight);
    });
  }

  function safeDraw(){
    try{
      if (document.fonts && document.fonts.ready){
        document.fonts.ready.then(function(){ draw(nameInput ? nameInput.value : ""); });
      }
      draw(nameInput ? nameInput.value : "");
    }catch(e){ draw(nameInput ? nameInput.value : ""); }
  }

  if (nameInput) nameInput.addEventListener("input", safeDraw);
  safeDraw();

  if (downloadBtn){
    downloadBtn.addEventListener("click", function(){
      var name = (nameInput ? nameInput.value.trim() : "") || "certificate";
      var link = document.createElement("a");
      link.download = "global-warming-explorer-certificate-" + name.replace(/\s+/g, "-").toLowerCase() + ".png";
      link.href = canvas.toDataURL("image/png");
      link.click();
    });
  }
})();
