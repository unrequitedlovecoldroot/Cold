def input_with_back(prompt="> "):
    """使用者輸入，若輸入 back 回上一層"""
    user_input = input(prompt).strip()
    if user_input.lower() == "back":
        return "BACK"
    return user_input
