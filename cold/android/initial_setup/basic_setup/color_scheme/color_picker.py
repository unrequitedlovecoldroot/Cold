from cold.tools.clear_screen import clear_screen

def picker_menu():
    while True:
        clear_screen()
        print("選色方式")
        print("1. 預設色系")
        print("2. 自訂 → 輸入十六進位")
        print("3. 選色盤（模擬）")
        print("back. 返回上層")
        choice = input("請選擇: ").strip().lower()
        if choice in ["1","2","3"]:
            print(f"已選擇方式 {choice}（模擬）")
        elif choice == "back":
            return
        else:
            print("無效選項")
        input("按 Enter 繼續...")
