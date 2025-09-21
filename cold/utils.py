import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def input_choice(prompt, choices):
    while True:
        choice = input(prompt).strip().lower()
        if choice in choices:
            return choice
        print("輸入錯誤，請重新輸入。")

def wait_enter():
    input("按 Enter 繼續...")

