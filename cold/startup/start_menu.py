from utils import clear_screen, input_with_back
from .device_selection import device_selection

def start_menu():
    while True:
        clear_screen()
        print("🎉 Cold 初始化系統")
        print("1️⃣ ▶️ 啟動")
        print("2️⃣ ⏹️ 關閉")
        choice = input_with_back("選擇操作: ")

        if choice == "1":
            device_selection()
        elif choice == "2":
            print("系統關閉中...")
            exit(0)
        elif choice == "BACK":
            return
        else:
            print("請輸入正確選項")
            input("按 Enter 繼續...")
