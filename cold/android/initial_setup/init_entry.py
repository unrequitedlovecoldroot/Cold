from cold.tools.screen_tools import clear_screen
from cold.tools.input_tools import input_with_back
from cold.tools.color_tools import Colors

def init_entry(menu_type, flags):
    while True:
        clear_screen()
        print(f"🏗️ {menu_type} 選單 (模擬功能)")
        print(f"{Colors.OKCYAN}此處為模擬選單，功能尚未實作{Colors.ENDC}")
        print("輸入 back 返回上一層")
        user_input = input_with_back("操作: ")
        if user_input == "BACK":
            flags[menu_type] = True  # 返回後標記已完成
            return
