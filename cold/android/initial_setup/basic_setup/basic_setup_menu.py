from cold.utils import clear_screen, wait_enter

def basic_setup_menu():
    clear_screen()
    print("🔹 基本設定選單")
    print("模擬語言 / 顏色方案 / 恢復預設")
    wait_enter()
    return True
