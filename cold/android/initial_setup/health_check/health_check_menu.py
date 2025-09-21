from cold.utils import clear_screen, wait_enter

def health_check_menu():
    clear_screen()
    print("🔹 初步系統健檢")
    print("模擬檢查 Python 套件 / Termux 工具")
    wait_enter()
    return True
