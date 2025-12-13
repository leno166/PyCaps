"""
@文件: hotkeys.py
@作者: 雷小鸥
@日期: 2025/12/2 20:56
@许可: MIT License
@描述: 
@版本: Version 1.0
"""
import keyboard as kb
from keyboard import on_release

CAPSLOCK_DOWN = False
ONLY_CAPSLOCK = True

# 使用字典来记录按下的键和对应的模拟键
PRESSED_KEYS = {}  # 格式: {'a': 'left', ...}


def on_key(event: kb.KeyboardEvent):
    global CAPSLOCK_DOWN, ONLY_CAPSLOCK, PRESSED_KEYS

    # print(event.name, event.event_type, CAPSLOCK_DOWN, ONLY_CAPSLOCK)

    # 处理CapsLock按下
    if event.event_type == kb.KEY_DOWN and event.name == 'caps lock':
        if ONLY_CAPSLOCK:
            # print('caps lock pressed - entering combo mode')
            CAPSLOCK_DOWN = True
            return None  # 抑制原始CapsLock事件

    # 处理CapsLock释放
    elif event.event_type == kb.KEY_UP and event.name == 'caps lock':
        # print('caps lock released')
        CAPSLOCK_DOWN = False

        # 释放所有按下的模拟键
        for key_name in list(PRESSED_KEYS.keys()):
            sim_key = PRESSED_KEYS[key_name]
            kb.send(sim_key, do_press=False, do_release=True)
            del PRESSED_KEYS[key_name]
            # print(f'Released simulated key: {sim_key}')

        # 如果只按了CapsLock，则发送实际的CapsLock切换
        if ONLY_CAPSLOCK:
            kb.send('caps lock')
            # print('Sent actual caps lock')

        ONLY_CAPSLOCK = True
        return None

    # 在CapsLock组合键模式下处理其他键按下
    if event.event_type == kb.KEY_DOWN and CAPSLOCK_DOWN:
        key_name = event.name.lower()
        # print(f'Key down in combo: {key_name}')

        if key_name == 'a':
            kb.send('left', do_press=True, do_release=False)
            PRESSED_KEYS[key_name] = 'left'
            ONLY_CAPSLOCK = False
            return None

        # 可以添加更多映射
        elif key_name == 'd':
            kb.send('right', do_press=True, do_release=False)
            PRESSED_KEYS[key_name] = 'right'
            ONLY_CAPSLOCK = False
            return None

        elif key_name == 's':
            kb.send('down', do_press=True, do_release=False)
            PRESSED_KEYS[key_name] = 'down'
            ONLY_CAPSLOCK = False
            return None

        elif key_name == 'w':
            kb.send('up', do_press=True, do_release=False)
            PRESSED_KEYS[key_name] = 'up'
            ONLY_CAPSLOCK = False
            return None

        # 其他键不做处理
        return event

    # 在CapsLock组合键模式下处理其他键释放
    elif event.event_type == kb.KEY_UP and CAPSLOCK_DOWN:
        key_name = event.name.lower()

        if key_name in PRESSED_KEYS:
            sim_key = PRESSED_KEYS[key_name]
            kb.send(sim_key, do_press=False, do_release=True)
            del PRESSED_KEYS[key_name]
            # print(f'Released simulated key: {sim_key}')
            return None

    # 不在CapsLock模式下的事件正常传递
    return event


def hook():
    kb.hook(on_key, suppress=True)


def unhook():
    kb.unhook_all()
