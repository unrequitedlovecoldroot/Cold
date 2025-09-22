from utils import clear_screen, input_with_back
from .launch import launch

def device_selection():
    while True:
        clear_screen()
        print("📱 裝置選擇")
        print("1️⃣ 安卓")
        print("2️⃣ iOS")
        choice = input_with_back("選擇裝置: ")

        if choice == "1":
            launch("android")
            return
        elif choice == "2":
            launch("ios")
            return
        elif choice == "BACK":
            return
        else:
            print("請輸入正確選項")
            input("按 Enter 繼續...")
