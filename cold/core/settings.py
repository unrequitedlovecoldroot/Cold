import json
import os

STORAGE_PATH = os.path.join(os.path.dirname(__file__), '..', 'storage', 'users', 'example_user')
SETTINGS_FILE = os.path.join(STORAGE_PATH, 'settings.json')

DEFAULT_SETTINGS = {
    "language": "中文",
    "colors": {
        "background_main": "#000000",
        "background_secondary": "#1c1c1c",
        "text_title": "#00ffff",
        "text_content": "#ffffff",
        "button_main": "#00ff00",
        "button_secondary": "#ff00ff",
        "border": "#ffffff",
        "label": "#ffff00",
        "notification": "#ff6600"
    },
    "flags": {
        "basic_setup_done": False,
        "tutorial_done": False,
        "system_settings_done": False,
        "health_check_done": False
    }
}

def load_settings():
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return DEFAULT_SETTINGS.copy()

def save_settings(settings):
    os.makedirs(STORAGE_PATH, exist_ok=True)
    with open(SETTINGS_FILE, 'w', encoding='utf-8') as f:
        json.dump(settings, f, ensure_ascii=False, indent=2)
