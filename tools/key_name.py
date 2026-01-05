"""
@文件: key_name.py
@作者: 雷小鸥
@日期: 2026/1/5 10:53
@许可: MIT License
@描述: 
@版本: Version 1.0
"""
import keyboard as kb
import time

def on_key(event):
    print(event.name)

kb.hook(on_key)

time.sleep(100)
