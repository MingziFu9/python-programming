# 实验代码

按章存放，`chNN/` 对应第 NN 章，文件名为 `labN_M_英文短名.py`（第 N 章实验 N-M），公共数据放在 `data/`，见 `data/README.md`。

第 1～9 章只用 Python 自带的功能，装好 Thonny（自带 Python 3.14）就能运行；第 10 章起要用到第三方库，安装方法：

```bash
pip install -r requirements.txt -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple
```

**运行方法**：在 Thonny 里打开 `chNN/` 下的 `.py` 文件，点绿色的“运行”按钮。读取数据的程序用 `../data/文件名` 找数据，所以要保持 `labs/` 文件夹的结构不变。

需要输入的程序（用到 `input()`），教材“运行结果”中提示文字（如“请输入数量：”）后面的内容不是程序打印的，而是编者当时输入的内容，和你在 Thonny 中看到的一样。

第 11 章另附 Jupyter 笔记本 `ch11/lab11_1_questions.ipynb`；第 12 章的实验 12-2、12-3 要先运行 `ch12/mock_llm_server.py`（模拟大模型服务器），见教材 12.3 节。
