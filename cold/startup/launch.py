from utils import clear_screen, input_with_back, Colors
from android.initial_setup.init_entry import init_entry

# 模擬 2~5 flag 狀態
flags = {
    "basic_setup": False,
    "tutorial": False,
    "system_settings": False,
    "health_check": False
}

def launch(platform):
    while True:
        clear_screen()
        print(f"🔌 啟動流程 ({platform})")
        print(f"2️⃣ 基本設定: {Colors.OKGREEN if flags['basic_setup'] else Colors.WARNING}已完成{Colors.ENDC if flags['basic_setup'] else Colors.ENDC}")
        print(f"3️⃣ 說明與教學: {Colors.OKGREEN if flags['tutorial'] else Colors.WARNING}已完成{Colors.ENDC if flags['tutorial'] else Colors.ENDC}")
        print(f"4️⃣ 系統需開啟設定: {Colors.OKGREEN if flags['system_settings'] else Colors.WARNING}已完成{Colors.ENDC if flags['system_settings'] else Colors.ENDC}")
        print(f"5️⃣ 初步系統健檢: {Colors.OKGREEN if flags['health_check'] else Colors.WARNING}已完成{Colors.ENDC if flags['health_check'] else Colors.ENDC}")
        print("6️⃣ ▶️ 開始按鈕 (完成 2~5 後才可啟動)")
        print("輸入 2~5 可進入對應選單，或輸入 back 返回")
        choice = input_with_back("選擇操作: ")

        if choice == "2":
            init_entry("basic_setup", flags)
        elif choice == "3":
            init_entry("tutorial", flags)
        elif choice == "4":
            init_entry("system_settings", flags)
        elif choice == "5":
            init_entry("health_check", flags)
        elif choice == "6":
            if all(flags.values()):
                print("🎉 Cold 初始化完成，進入系統主程式...")
                input("按 Enter 繼續...")
                return
            else:
                print(f"{Colors.FAIL}請先完成所有初始設定 (2~5){Colors.ENDC}")
                input("按 Enter 繼續...")
        elif choice == "BACK":
            return
        else:
            print("請輸入正確選項")
            input("按 Enter 繼續...")
