from cold.utils import pause, clear_screen

def select_language():
    clear_screen()
    print("[語言設定]")
    print("1️⃣ 中文")
    print("2️⃣ 英文")
    choice = input("選擇語言: ")
    if choice == "1":
        print("已選擇中文")
    elif choice == "2":
        print("已選擇英文")
    else:
        print("輸入錯誤")
    pause()
