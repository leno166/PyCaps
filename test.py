"""
@文件: hotkeys.py
@作者: 雷小鸥
@日期: 2025/12/2 20:56
@许可: MIT License
@描述:
@版本: Version 1.0
"""
import keyboard as kb

CAPSLOCK_DOWN = False
ONLY_CAPSLOCK = True

# 记录当前的重映射处理器，用于后续移除
current_remap_handler = None

def on_key(event: kb.KeyboardEvent):
    global CAPSLOCK_DOWN, ONLY_CAPSLOCK, current_remap_handler

    # 处理CapsLock按下
    if event.event_type == kb.KEY_DOWN and event.name == 'caps lock':
        if ONLY_CAPSLOCK:
            CAPSLOCK_DOWN = True
            print("CapsLock进入组合键模式")

            # 动态注册按键重映射
            if current_remap_handler is None:
                # 将 a 映射到 left
                current_remap_handler = kb.remap_key('a', 'left')
                print("已注册 a -> left 映射")

            return None  # 抑制原始CapsLock事件

    # 处理CapsLock释放
    elif event.event_type == kb.KEY_UP and event.name == 'caps lock':
        print("CapsLock释放")
        CAPSLOCK_DOWN = False

        # 移除动态注册的重映射
        if current_remap_handler is not None:
            kb.unremap_key(current_remap_handler)
            current_remap_handler = None
            print("已移除 a -> left 映射")

        # 如果只按了CapsLock，则发送实际的CapsLock切换
        if ONLY_CAPSLOCK:
            kb.send('caps lock')
            print("发送实际CapsLock切换")

        ONLY_CAPSLOCK = True
        return None

    # 在CapsLock组合键模式下处理其他键按下
    if event.event_type == kb.KEY_DOWN and CAPSLOCK_DOWN:
        key_name = event.name.lower()

        # 检查是否是已经被重映射的键
        if key_name == 'a':
            ONLY_CAPSLOCK = False
            # remap_key会自动处理，这里只需记录状态
            print(f"在组合键模式下按下 {key_name}，将映射为 left")

        # 其他键正常传递
        return event

    # 在CapsLock组合键模式下处理其他键释放
    elif event.event_type == kb.KEY_UP and CAPSLOCK_DOWN:
        key_name = event.name.lower()

        if key_name == 'a':
            print(f"在组合键模式下释放 {key_name}")

        return event

    # 不在CapsLock模式下的事件正常传递
    return event

def hook():
    # 使用监控版本以便调试
    kb.hook(on_key, suppress=True)
    print("Hotkey hook已安装")

def unhook():
    # 清理可能存在的重映射
    if current_remap_handler is not None:
        kb.unremap_key(current_remap_handler)
        print("清理重映射")

    kb.unhook_all()
    print("Hotkey hook已移除")

hook()

kb.wait('esc')