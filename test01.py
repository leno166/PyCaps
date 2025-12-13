"""
@文件: test01.py
@作者: 雷小鸥
@日期: 2025/12/2 22:34
@许可: MIT License
@描述: 
@版本: Version 1.0
"""
import keyboard as kb
import time

time.sleep(3)


kb.send('shift', do_press=True, do_release=False)

kb.send('left', do_press=True, do_release=True)
time.sleep(0.1)

kb.send('left', do_press=True, do_release=True)
time.sleep(0.1)

kb.send('left', do_press=True, do_release=True)
kb.send('left', do_press=True, do_release=True)

kb.send('shift', do_press=False, do_release=True)

