from cold.utils import clear_screen
from cold.android.initial_setup.init_entry import initial_setup_android

def device_selection():
    clear_screen()
    print("📱 裝置選擇")
    print("1. 安卓")
    print("2. iOS")
    choice = input("選擇設備 (1/2): ").strip()
    if choice == "1":
        initial_setup_android()
    elif choice == "2":
        print("iOS 功能待擴充")
    else:
        print("無效選項")
        device_selection()
