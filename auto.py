"""
@文件: auto.py
@作者: 雷小鸥
@日期: 2026/1/2 17:51
@许可: MIT License
@描述: 
@版本: Version 1.0
"""
import uiautomation as ui


def move_caret_left():
    # 1. 当前获得焦点的控件
    ctrl = ui.GetFocusedControl()
    if not ctrl:
        return

    # 2. 获取 TextPattern
    tp = ctrl.Get()
    if not tp:
        return
