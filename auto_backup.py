# auto_backup.py
import subprocess
import datetime

# 记录日志
now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(f"[{now}] 正在自动备份备忘录为 PDF...")

# 调用 export 命令
subprocess.run(["python", "memo.py", "export", "pdf"])