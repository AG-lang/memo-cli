📘 命令行备忘录工具（Memo CLI）
一个基于 Python 的命令行备忘录工具，支持添加、查看、删除、搜索、分类（可扩展）和导出功能，适合日常记录、任务管理、学习笔记等。

✅ 已支持导出为 TXT / Markdown / CSV / PDF（含中文）
✅ 支持自动命名导出文件
✅ 支持自动备份脚本（可配合系统定时任务）

🧰 技术栈
Python 3.6+
JSON 数据存储
argparse 命令行解析
reportlab PDF 导出
csv 模块
系统任务调度（可选）
📦 功能概览
功能 命令示例
✅ 添加备忘录 python memo.py add "学习 Git"
✅ 查看所有备忘录 python memo.py list
✅ 删除指定备忘录 python memo.py delete 1
✅ 搜索关键词 python memo.py search git
✅ 导出 TXT python memo.py export txt
✅ 导出 Markdown python memo.py export md
✅ 导出 CSV python memo.py export csv
✅ 导出 PDF（支持中文） python memo.py export pdf
✅ 自动备份脚本 python auto_backup.py
🛠️ 安装依赖

pip install reportlab
📁 项目结构

memo-cli/
├── memo.py # 主程序
├── auto_backup.py # 自动备份脚本（可选）
├── memo.json # 数据文件（自动生成）
├── exports/ # 导出文件保存目录
│ ├── memos_2024-04-13.pdf
├── fonts/ # 中文字体目录
│ └── MSYH.TTC # 微软雅黑（支持 PDF 中文）
├── .gitignore
└── README.md
📄 字体说明（PDF 中文支持）
为了支持 PDF 中文导出，你需要准备一个中文字体文件（如：微软雅黑）：

打开 C:\Windows\Fonts，复制 MSYH.TTC 到项目的 fonts/ 目录。
程序中使用如下方式注册字体：

from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(TTFont("MSYH", "fonts/MSYH.TTC"))
🕒 自动备份功能（可选）
你可以使用 auto_backup.py 实现每天自动导出 PDF 备份：

python auto_backup.py
配合系统任务计划使用：
Windows：使用“任务计划程序”设置每天定时执行
Linux/macOS：使用 crontab
🧪 示例演示

# 添加备忘录

python memo.py add "学习 Python"

# 查看备忘录

python memo.py list

# 删除第 1 条

python memo.py delete 1

# 搜索关键词

python memo.py search git

# 导出为 PDF

python memo.py export pdf
