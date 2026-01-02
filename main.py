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
import sys
import os
from pathlib import Path

RUNNING = True
RUNNING_R_LOCK = RLock()
RUNNING_LOCK = Lock()

if hasattr(sys, '_MEIPASS'):
    ROOT_PATH = Path(sys._MEIPASS)
else:
    ROOT_PATH = Path('.')

LOGO = ROOT_PATH / 'logo.ico'
print(LOGO)

def on_tray_quit(tray: SysTrayIcon):
    unhook()

    global RUNNING
    with RUNNING_LOCK:
        RUNNING = False


def main():
    with SysTrayIcon(icon=str(LOGO), hover_text='caps+', on_quit=on_tray_quit):
        hook()

        with RUNNING_R_LOCK:
            while RUNNING:
                time.sleep(1)


if __name__ == '__main__':
    main()
