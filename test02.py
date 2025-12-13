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

        # 清理按下的键（注意：此时所有模拟键已经释放）
        PRESSED_KEYS.clear()

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
            # 点按效果：同时按下和释放左箭头
            kb.send('left')
            PRESSED_KEYS[key_name] = 'left'  # 记录按下的键
            ONLY_CAPSLOCK = False
            return None

        # 可以添加更多映射
        elif key_name == 'd':
            kb.send('right')
            PRESSED_KEYS[key_name] = 'right'
            ONLY_CAPSLOCK = False
            return None

        elif key_name == 's':
            kb.send('down')
            PRESSED_KEYS[key_name] = 'down'
            ONLY_CAPSLOCK = False
            return None

        elif key_name == 'w':
            kb.send('up')
            PRESSED_KEYS[key_name] = 'up'
            ONLY_CAPSLOCK = False
            return None

        # 其他键不做处理
        return event

    # 在CapsLock组合键模式下处理其他键释放
    elif event.event_type == kb.KEY_UP and CAPSLOCK_DOWN:
        key_name = event.name.lower()

        if key_name in PRESSED_KEYS:
            # 对于点按效果，释放时不需要做任何操作
            # 因为我们在按下时已经完成了完整的按键
            del PRESSED_KEYS[key_name]
            return None

    # 不在CapsLock模式下的事件正常传递
    return event


def monitor(event: kb.KeyboardEvent):
    event = on_key(event)
    if event:
        print(event.to_json())
    else:
        print("Event suppressed")
    return event


def hook():
    kb.hook(monitor, suppress=True)


def unhook():
    kb.unhook_all()


# 测试代码
if __name__ == "__main__":
    hook()
    print("按下Esc退出...")
    kb.wait('esc')
    unhook()