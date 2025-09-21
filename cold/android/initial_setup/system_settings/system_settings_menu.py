from cold.utils import clear_screen, wait_enter

def system_settings_menu():
    clear_screen()
    print("🔹 系統需開啟設定")
    print("模擬無障礙 / 通知 / 電池 / Termux 權限檢查")
    wait_enter()
    return True
