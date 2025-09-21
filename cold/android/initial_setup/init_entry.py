from cold.utils import clear_screen, wait_enter
from cold.android.initial_setup.basic_setup.basic_setup_menu import basic_setup_menu
from cold.android.initial_setup.tutorial.tutorial_menu import tutorial_menu
from cold.android.initial_setup.system_settings.system_settings_menu import system_settings_menu
from cold.android.initial_setup.health_check.health_check_menu import health_check_menu
from cold.android.start_button import start_button

# flags 追蹤 2~5 完成狀態
setup_flags = {
    "basic": False,
    "tutorial": False,
    "system_settings": False,
    "health_check": False
}

def initial_setup():
    while True:
        clear_screen()
        print("⚙️ 初始設定流程（入口）")
        print(f"1. 2️⃣ 基本設定 [{'✅' if setup_flags['basic'] else '❌'}]")
        print(f"2. 3️⃣ 說明與教學 [{'✅' if setup_flags['tutorial'] else '❌'}]")
        print(f"3. 4️⃣ 系統需開啟設定 [{'✅' if setup_flags['system_settings'] else '❌'}]")
        print(f"4. 5️⃣ 初步系統健檢 [{'✅' if setup_flags['health_check'] else '❌'}]")
        print("5. ▶️ 開始按鈕 (完成 2~5 後顯示)")
        print("輸入 back 返回")
        choice = input("選擇操作: ").strip().lower()
        if choice == "1":
            setup_flags['basic'] = basic_setup_menu()
        elif choice == "2":
            setup_flags['tutorial'] = tutorial_menu()
        elif choice == "3":
            setup_flags['system_settings'] = system_settings_menu()
        elif choice == "4":
            setup_flags['health_check'] = health_check_menu()
        elif choice == "5":
            if all(setup_flags.values()):
                start_button()
            else:
                print("請先完成 2~5 所有項目")
                wait_enter()
        elif choice == "back":
            break
