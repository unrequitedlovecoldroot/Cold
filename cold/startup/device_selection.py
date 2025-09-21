from cold.utils import clear_screen
from cold.android.initial_setup.init_entry import initial_setup

def device_selection():
    clear_screen()
    print("📱 裝置選擇")
    print("1. 安卓")
    print("2. iOS (待擴充)")
    choice = input("選擇設備: ").strip()
    if choice == "1":
        initial_setup()
    else:
        print("iOS 功能尚未實裝")
