from cold.utils import clear_screen, pause
from cold.settings import language, color, tutorial, system, health_check
from cold.error_report import report

def main_menu():
    while True:
        clear_screen()
        print("Cold 專案 🔌 啟動選單")
        print("1️⃣ 啟動")
        print("2️⃣ 錯誤回報")
        print("3️⃣ 關閉")
        choice = input("請選擇: ")

        if choice == "1":
            start_menu()
        elif choice == "2":
            report.main_report()
        elif choice == "3":
            break
        else:
            print("輸入錯誤，請重新選擇")
            pause()

def start_menu():
    clear_screen()
    print("📱 裝置選擇")
    print("1️⃣ 安卓")
    print("2️⃣ iOS (待擴充)")
    print("3️⃣ 返回")
    choice = input("請選擇: ")

    if choice == "1":
        android_setup()
    elif choice == "2":
        print("iOS 功能待擴充")
        pause()
    elif choice == "3":
        return
    else:
        print("輸入錯誤")
        pause()

def android_setup():
    clear_screen()
    print("⚙️ 初始設定流程（入口）")
    # 2~5 初始設定流程
    language.select_language()
    color.select_color()
    tutorial.show_tutorial()
    system.check_system_settings()
    health_check.run_health_check()
    print("✅ 初始設定完成，可按開始進入使用者模式")
    pause()
    # 之後可以連接使用者模式選擇 ROOT/NoROOT
