from cold.tools.clear_screen import clear_screen

def category_menu():
    while True:
        clear_screen()
        print("大分類選擇")
        print("1. 背景")
        print("2. 文字")
        print("3. 按鈕")
        print("4. 邊框")
        print("5. 標籤")
        print("6. 通知")
        print("back. 返回上層")
        choice = input("請選擇: ").strip().lower()
        if choice in ["1","2","3","4","5","6"]:
            print(f"已選擇 {choice} 分類（模擬）")
        elif choice == "back":
            return
        else:
            print("無效選項")
        input("按 Enter 繼續...")
