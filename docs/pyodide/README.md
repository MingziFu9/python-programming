# Pyodide（网页“试一试”运行器）

本目录是 [Pyodide](https://pyodide.org/) 0.28.3 的核心文件（Mozilla Public License 2.0），
从 npm 包 `pyodide@0.28.3` 中原样复制，用于在浏览器里运行正文中的“试一试”代码，
不依赖外部网站。只包含 Python 标准库，不含 NumPy、pandas 等第三方库。

升级方法：`npm pack pyodide@<版本>`，解压后把 pyodide.js、pyodide.asm.js、pyodide.asm.wasm、
python_stdlib.zip、pyodide-lock.json 五个文件复制到这里。
