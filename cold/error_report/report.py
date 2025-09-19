from cold.utils import pause, clear_screen

def main_report():
    clear_screen()
    print("[錯誤回報入口]")
    print("1️⃣ 提交回報")
    print("2️⃣ 草稿管理")
    print("3️⃣ 統計")
    print("4️⃣ 返回")
    choice = input("請選擇: ")
    if choice == "4":
        return
    else:
        print("功能示範，暫不實作")
        pause()
