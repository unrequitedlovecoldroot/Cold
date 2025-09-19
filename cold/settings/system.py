from cold.utils import pause, clear_screen

def check_system_settings():
    clear_screen()
    print("[系統需開啟設定]")
    print("1️⃣ 無障礙")
    print("2️⃣ 通知存取")
    print("3️⃣ 電池優化排除")
    print("4️⃣ Termux 權限")
    pause("請確認已開啟所需設定，按 Enter 繼續")
