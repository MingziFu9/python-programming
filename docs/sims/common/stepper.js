// 代码单步执行器：多个动画共用。
// 用法：Stepper(容器元素, 程序列表)；程序列表的每一项是 {title, trace, notes}
//   trace 由 tools/make_trace.py 真实运行代码生成：{code: [...行], steps: [{line, frames, out, ret?, error?}]}
//   notes 是 {行号: "这一行在做什么"}，可选
(function () {
  function esc(s) { return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;"); }

  window.Stepper = function (root, programs) {
    var prog = 0, i = 0, timer = null;
    root.innerHTML =
      '<div class="row st-tabs"></div>' +
      '<div class="grid2">' +
      '  <div class="box"><h2>代码（<span class="st-arrow">➜</span> 是下一步要执行的行）</h2><pre class="st-code"></pre></div>' +
      '  <div><div class="box"><h2>变量</h2><div class="st-vars"></div></div>' +
      '       <div class="box"><h2>输出</h2><pre class="st-out"></pre></div></div>' +
      '</div>' +
      '<div class="row"><button class="st-first">⏮ 重来</button><button class="st-prev">◀ 上一步</button>' +
      '<button class="main st-next">下一步 ▶</button><button class="st-play">▶▶ 自动播放</button>' +
      '<span class="note st-count"></span></div>' +
      '<div class="msg st-msg"></div>';
    var $ = function (c) { return root.querySelector(c); };

    var tabs = $(".st-tabs");
    if (programs.length > 1) {
      programs.forEach(function (p, k) {
        var b = document.createElement("button");
        b.textContent = p.title;
        b.onclick = function () { prog = k; i = 0; stop(); render(); };
        tabs.appendChild(b);
      });
    } else { tabs.style.display = "none"; }

    function stop() { if (timer) { clearInterval(timer); timer = null; } $(".st-play").textContent = "▶▶ 自动播放"; }

    function render() {
      var p = programs[prog], tr = p.trace, st = tr.steps[i], prev = i > 0 ? tr.steps[i - 1] : null;
      Array.prototype.forEach.call(tabs.children, function (b, k) { b.className = k === prog ? "on" : ""; });
      var html = tr.code.map(function (c, k) {
        var n = k + 1, cls = "st-line";
        if (st.line === n) cls += " st-next-line";
        else if (prev && prev.line === n) cls += " st-done-line";
        var mark = st.line === n ? "➜" : (prev && prev.line === n ? "✓" : " ");
        return '<span class="' + cls + '"><span class="st-no">' + mark + " " + (n < 10 ? " " : "") + n + "</span> " + esc(c) + "</span>";
      }).join("");
      $(".st-code").innerHTML = html;
      var vs = st.frames.map(function (f) {
        var keys = Object.keys(f.vars);
        var rows = keys.length ? keys.map(function (k) {
          var changed = !prev || !prev.frames.some(function (pf) { return pf.name === f.name && pf.vars[k] === f.vars[k]; });
          return "<tr" + (changed ? ' class="st-chg"' : "") + "><td><code>" + esc(k) + "</code></td><td><code>" + esc(f.vars[k]) + "</code></td></tr>";
        }).join("") : '<tr><td colspan="2" class="note">（还没有变量）</td></tr>';
        return '<div class="st-frame"><div class="st-fname">' + esc(f.name) + '</div><table class="t">' + rows + "</table></div>";
      }).join("");
      $(".st-vars").innerHTML = vs;
      $(".st-out").textContent = st.out || " ";
      var msg = "";
      if (st.error) msg = '<span class="bad">程序出错停止：' + esc(st.error) + "</span>";
      else if (st.line === null) msg = '<span class="ok">程序运行结束。</span>';
      else if (st.ret !== undefined) msg = "函数执行完毕，带着返回值 <code>" + esc(st.ret) + "</code> 回到调用它的地方。";
      else if (p.notes && p.notes[st.line]) msg = "下一步：" + p.notes[st.line];
      $(".st-msg").innerHTML = msg;
      $(".st-count").textContent = "第 " + (i + 1) + " / " + tr.steps.length + " 步";
      $(".st-prev").disabled = $(".st-first").disabled = i === 0;
      $(".st-next").disabled = i === tr.steps.length - 1;
    }
    function next() { var n = programs[prog].trace.steps.length; if (i < n - 1) { i++; render(); } else stop(); }
    $(".st-next").onclick = function () { stop(); next(); };
    $(".st-prev").onclick = function () { stop(); if (i > 0) { i--; render(); } };
    $(".st-first").onclick = function () { stop(); i = 0; render(); };
    $(".st-play").onclick = function () {
      if (timer) { stop(); return; }
      if (i === programs[prog].trace.steps.length - 1) i = 0;
      this.textContent = "⏸ 暂停";
      timer = setInterval(next, 900);
    };
    render();
  };
})();
