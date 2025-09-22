from cold.tools.clear_screen import clear_screen

def detail_menu():
    while True:
        clear_screen()
        print("細分類選擇")
        print("1. 主背景")
        print("2. 次背景")
        print("3. 標題文字")
        print("4. 內容文字")
        print("5. 主按鈕")
        print("6. 次按鈕")
        print("7. 邊框線")
        print("8. 標籤顏色")
        print("back. 返回上層")
        choice = input("請選擇: ").strip().lower()
        if choice in [str(i) for i in range(1,9)]:
            print(f"已選擇 {choice} 細分類（模擬）")
        elif choice == "back":
            return
        else:
            print("無效選項")
        input("按 Enter 繼續...")
