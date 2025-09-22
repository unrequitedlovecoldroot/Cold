from cold.core.settings import load_settings, save_settings

def restore_defaults():
    settings = load_settings()
    settings["colors"] = {
        "background_main": "#000000",
        "background_secondary": "#1c1c1c",
        "text_title": "#00ffff",
        "text_content": "#ffffff",
        "button_main": "#00ff00",
        "button_secondary": "#ff00ff",
        "border": "#ffffff",
        "label": "#ffff00",
        "notification": "#ff6600"
    }
    save_settings(settings)
    print("已恢復預設顏色")
