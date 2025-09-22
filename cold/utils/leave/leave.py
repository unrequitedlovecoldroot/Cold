import sys

def check_leave(user_input: str):
    """檢查使用者是否輸入 leave"""
    if user_input.strip().lower() == "leave":
        print("\n🚪 離開 Cold，已安全退出")
        sys.exit(0)
    return user_input
