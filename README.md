## 足球盘口查询工具

一个基于 Python 和 Streamlit 的简单查询界面，用来从 `ft.xlsx` 中按联赛和盘口信息筛选数据。

### 1. 安装环境

在终端进入项目目录：

```bash
cd /Users/wangpeiwei/Desktop/football
```

创建并激活虚拟环境（可选但推荐）：

```bash
python3 -m venv .venv
source .venv/bin/activate  # Windows 使用 .venv\Scripts\activate
```

安装依赖：

```bash
pip install -r requirements.txt
```

### 2. 运行查询界面

确保 `ft.xlsx` 和 `app.py` 在同一目录下（默认读取当前目录的 `ft.xlsx`）。

在终端运行：

```bash
streamlit run app.py
```

浏览器会自动打开一个页面（或终端里给出本地访问地址），看到“足球盘口查询工具”界面。

### 3. 使用方法

- **Excel 文件路径**：默认是当前目录下的 `ft.xlsx`，如有需要可以改成其它路径。
- **选择联赛（工作表）**：下拉选择需要查询的联赛类型（对应 Excel 的工作表标签，如“日职”、“日职乙”等）。
- **选择盘口列**：从当前工作表的所有列中选择存放盘口信息的那一列。
- **输入要匹配的盘口**：输入关键字进行模糊查询，例如：
  - `半球`
  - `平/半`
  - `半/一`

点击回车后，界面会显示匹配到的行数和筛选结果表格，并提供“下载筛选结果（CSV）”按钮导出数据。

