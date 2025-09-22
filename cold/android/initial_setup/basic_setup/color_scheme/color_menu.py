from .color_categories import category_menu
from .color_details import detail_menu
from .color_picker import picker_menu
from .restore_defaults import restore_defaults
from cold.tools.clear_screen import clear_screen

def color_menu():
    while True:
        clear_screen()
        print("🎨 顏色方案設定")
        print("1. 大分類")
        print("2. 細分類")
        print("3. 選色方式")
        print("4. ↩️ 恢復預設")
        print("back. 返回上層")
        choice = input("請選擇: ").strip().lower()
        if choice == "1":
            category_menu()
        elif choice == "2":
            detail_menu()
        elif choice == "3":
            picker_menu()
        elif choice == "4":
            restore_defaults()
        elif choice == "back":
            return
        else:
            print("無效選項")
        input("按 Enter 繼續...")
