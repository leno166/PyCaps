"""
@文件: main.py
@作者: 雷小鸥
@日期: 2025/12/2 20:51
@许可: MIT License
@描述: 
@版本: Version 1.0
"""
from infi.systray import SysTrayIcon
import time
from threading import Lock, RLock
from hotkeys import hook, unhook

RUNNING = True
RUNNING_R_LOCK = RLock()
RUNNING_LOCK = Lock()


def on_tray_quit(tray: SysTrayIcon):
    unhook()

    global RUNNING
    with RUNNING_LOCK:
        RUNNING = False


def main():
    with SysTrayIcon(icon=None, hover_text='caps+', on_quit=on_tray_quit):
        hook()

        with RUNNING_R_LOCK:
            while RUNNING:
                time.sleep(1)

if __name__ == '__main__':
    main()
