// “试一试”：在浏览器里直接运行正文中的 Python 代码。
// 写法：把代码块放进 <div class="tryit" markdown> ... </div>，页面上会出现“▶ 试一试”按钮。
// 运行器是本站自带的 Pyodide（docs/pyodide/，只含标准库），第一次点击需要下载约 12 MB，之后浏览器会缓存。
// input() 会弹出输入框；每次运行都是全新的环境，互不影响。
(function () {
  var pyPromise = null;

  function siteBase() {
    var s = document.querySelector('script[src*="javascripts/tryit.js"]');
    return s ? s.src.replace(/javascripts\/tryit\.js.*$/, "") : "/";
  }

  function loadScript(src) {
    return new Promise(function (ok, fail) {
      var el = document.createElement("script");
      el.src = src; el.onload = ok; el.onerror = fail;
      document.head.appendChild(el);
    });
  }

  function getPy() {
    if (!pyPromise) {
      var base = siteBase() + "pyodide/";
      pyPromise = loadScript(base + "pyodide.js").then(function () {
        return window.loadPyodide({ indexURL: base });
      });
    }
    return pyPromise;
  }

  function setup(box) {
    var codeEl = box.querySelector("code");
    if (!codeEl) return;
    var original = codeEl.innerText.replace(/\n$/, "");
    var bar = document.createElement("div");
    bar.className = "tryit-bar";
    var btn = document.createElement("button");
    btn.className = "tryit-btn";
    btn.textContent = "▶ 试一试";
    bar.appendChild(btn);
    box.appendChild(bar);

    btn.addEventListener("click", function () {
      var area = document.createElement("textarea");
      area.className = "tryit-code";
      area.value = original;
      area.spellcheck = false;
      area.rows = Math.min(Math.max(original.split("\n").length + 1, 3), 24);
      var run = document.createElement("button");
      run.className = "tryit-btn"; run.textContent = "▶ 运行";
      var reset = document.createElement("button");
      reset.className = "tryit-btn tryit-plain"; reset.textContent = "↺ 还原代码";
      var out = document.createElement("pre");
      out.className = "tryit-out"; out.textContent = "改一改上面的代码，然后点“运行”。";
      bar.innerHTML = "";
      bar.appendChild(run); bar.appendChild(reset);
      box.appendChild(area); box.appendChild(bar); box.appendChild(out);
      area.addEventListener("keydown", function (e) {
        if (e.key === "Tab") {           // Tab 键输入 4 个空格，而不是跳到下一个控件
          e.preventDefault();
          var s = area.selectionStart;
          area.value = area.value.slice(0, s) + "    " + area.value.slice(area.selectionEnd);
          area.selectionStart = area.selectionEnd = s + 4;
        }
      });
      reset.addEventListener("click", function () { area.value = original; });
      run.addEventListener("click", function () {
        run.disabled = true;
        out.className = "tryit-out";
        out.textContent = pyPromise ? "运行中……" : "第一次运行，正在加载 Python（约 12 MB，请稍候）……";
        getPy().then(function (py) {
          var text = "";
          var dec = new TextDecoder();
          var write = function (buf) { text += dec.decode(buf, { stream: true }); return buf.length; };
          py.setStdout({ write: write });
          py.setStderr({ write: write });
          py.setStdin({ stdin: function () {
            var last = text.split("\n").pop();          // input() 的提示文字
            var v = window.prompt(last || "程序在等待你输入（input）：");
            v = v === null ? "" : v;
            text += v + "\n";                          // 像终端一样把输入的内容显示出来
            return v;
          }, autoEOF: true });
          var g = py.globals.get("dict")();
          return py.runPythonAsync(area.value, { globals: g }).then(function () {
            out.textContent = text || "（程序运行完了，没有输出）";
          }, function (err) {
            var msg = String(err.message || err);
            var i = msg.indexOf('File "<exec>"');
            if (i >= 0) msg = "Traceback (most recent call last):\n  " + msg.slice(i);
            out.className = "tryit-out tryit-err";
            out.textContent = text + msg;
          }).finally(function () { g.destroy(); });
        }, function () {
          out.className = "tryit-out tryit-err";
          out.textContent = "加载 Python 失败，请检查网络后刷新页面重试。也可以把代码复制到 Thonny 里运行。";
        }).finally(function () { run.disabled = false; });
      });
      area.focus();
    });
  }

  function init() { document.querySelectorAll("div.tryit").forEach(setup); }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
