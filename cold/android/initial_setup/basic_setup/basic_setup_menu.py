from cold.utils import clear_screen

def basic_setup_menu():
    clear_screen()
    print("2️⃣ 基本設定")
    print("語言設定：")
    lang = input("選擇語言 (中文/英文/back): ").strip().lower()
    if lang == "back":
        return False
    print(f"已選擇語言：{lang}")

    print("顏色方案設定（模擬流程）")
    input("按 Enter 完成顏色方案選擇")

    restore = input("是否恢復預設 (Y/N): ").strip().lower()
    if restore == "y":
        print("已恢復預設")
    else:
        print("保留自訂顏色方案")

    return True
