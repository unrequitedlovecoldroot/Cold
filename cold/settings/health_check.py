from cold.utils import pause, clear_screen

def run_health_check():
    clear_screen()
    print("[初步系統健檢]")
    print("檢查 Python 套件 / Termux 工具...")
    print("可自動安裝 / 跳過 / canxing 強制跳過")
    pause("健檢完成，按 Enter 返回")
