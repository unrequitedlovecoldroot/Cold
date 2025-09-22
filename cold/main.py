from cold.utils.clear.clear import clear_screen
from cold.utils.leave.leave import check_leave


def main():
    while True:
        clear_screen()
        print("🔌 Cold 啟動選單")
        print("====================")
        print("1. ▶️ 啟動")
        print("2. ⏹️ 關閉")
        print("💡 輸入 `leave` 可隨時退出")
        print("====================")

        choice = check_leave(input("請選擇: "))

        if choice == "1":
            print("📱 裝置選擇 (模擬流程)...")
            check_leave(input("\n(按 Enter 繼續)"))
        elif choice == "2":
            print("\n🚪 離開 Cold，已安全退出")
            break
        else:
            print("⚠️ 無效選項")
            check_leave(input("\n(按 Enter 繼續)"))
