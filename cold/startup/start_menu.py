from cold.utils import clear_screen
from cold.startup.device_selection import device_selection

def start_menu():
    clear_screen()
    print("🎉 Cold 系統啟動選單")
    print("1. ▶️ 啟動")
    print("2. ⏹️ 關閉")
    choice = input("選擇操作: ").strip()
    if choice == "1":
        device_selection()
    else:
        print("系統已關閉")
