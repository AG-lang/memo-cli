# 命令行备忘录工具（Python）

一个简单的命令行备忘录程序，支持添加、查看、删除备忘录。

## 使用方法

```bash
python memo.py add "学习 Git"
python memo.py list
python memo.py delete 1
```

## 字体说明（PDF 中文支持）

本项目使用系统字体 `MSYH.TTC`（微软雅黑）以支持 PDF 中文导出。

如遇中文乱码，请：

1. 将字体文件 `MSYH.TTC` 放入项目 `fonts/` 文件夹
2. 修改代码使用：
   ```python
   TTFont("MSYH", "fonts/MSYH.TTC")
   ```
3. 如仍出错，可尝试：
   ```

   ```

TTFont("MSYH", "fonts/MSYH.TTC", subfontIndex=0)
