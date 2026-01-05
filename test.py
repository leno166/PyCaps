"""
@文件: hotkeys.py
@作者: 雷小鸥
@日期: 2025/12/2 20:56
@许可: MIT License
@描述:
@版本: Version 1.0
"""
import keyboard as kb
import time

time.sleep(1)

kb.send('ctrl+shift+#', do_press=True, do_release=True)