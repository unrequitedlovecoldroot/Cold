import os
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause(msg="按 Enter 繼續..."):
    input(msg)

def exit_program():
    print("退出 Cold 專案")
    sys.exit(0)
