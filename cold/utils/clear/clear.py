import os

def clear_screen():
    """清理螢幕"""
    os.system("clear" if os.name == "posix" else "cls")
