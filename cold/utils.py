import os
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def input_choice(prompt, choices, allow_back=False):
    while True:
        choice = input(prompt).strip()
        if allow_back and choice.lower() == 'back':
            return 'back'
        if choice in choices:
            return choice
        print(f"請輸入有效選項：{choices}")
