from cold.utils import clear_screen
from cold.android.initial_setup.basic_setup.basic_setup_menu import basic_setup_menu
from cold.android.initial_setup.tutorial.tutorial_menu import tutorial_menu
from cold.android.initial_setup.system_settings.system_settings_menu import system_settings_menu
from cold.android.initial_setup.health_check.health_check_menu import health_check_menu

flags = {
    "basic_setup": False,
    "tutorial": False,
    "system_settings": False,
    "health_check": False
}

def initial_setup_android():
    while True:
        clear_screen()
        print("⚙️ 初始設定流程（入口）")
        for i, key in enumerate(flags.keys(), start=2):
            status = "✅" if flags[key] else "❌"
            print(f"{i}. {key} {status}")
        print("start. ▶️ 開始按鈕 (完成 2~5 後可點)")
        choice = input("選擇流程 (輸入數字/start/back): ").strip().lower()

        if choice == "2":
            flags["basic_setup"] = basic_setup_menu()
        elif choice == "3":
            flags["tutorial"] = tutorial_menu()
        elif choice == "4":
            flags["system_settings"] = system_settings_menu()
        elif choice == "5":
            flags["health_check"] = health_check_menu()
        elif choice == "start":
            if all(flags.values()):
                print("🎉 Cold 初始化完成，進入系統主程式...")
                from cold.android.user_mode.user_mode_menu import user_mode_menu
                user_mode_menu()
                break
            else:
                print("請完成所有必須流程才可開始")
        elif choice == "back":
            return
        else:
            print("無效選項")
