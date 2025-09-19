# cold/__init__.py

"""
Cold 套件初始化檔案
Author: Cold
Description: 初始化 Cold 套件，確保 main.py 可正確引用。
"""

# 這裡可以放套件全域設定、版本資訊
__version__ = "0.1.0"
__author__ = "Cold"

# 可以在此初始化一些全域變數或設定
COLD_CONFIG = {
    "language": "zh",
    "theme": "default",
    "user_mode": None,  # ROOT / NoROOT
}

# 如果未來要自動載入其他模組，可以在此引入
# from . import utils
# from . import menu
