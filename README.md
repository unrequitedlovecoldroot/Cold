# Cold 專案開發準則 v1.5（權威版）

## 一、專案概述
Cold 是專為 Termux 環境設計的模組化自動化專案，支援 Android/iOS，提供啟動選單、使用者模式、腳本管理、日誌管理、個人設定、教學、系統健檢與錯誤回報。  
入口：`python -m cold`  

---

## 二、完整專案目錄結構

Cold/
├─ pyproject.toml # PyPI 打包核心設定
├─ setup.cfg # 補充設定 (描述/分類等)
├─ setup.py # 舊版相容，呼叫 pyproject
├─ README.md # 專案說明文件
├─ LICENSE # 授權條款
├─ MANIFEST.in # 控制打包哪些檔案
├─ requirements.txt # 依賴套件清單
├─ .gitignore # 避免推送不必要檔案 (含 storage/)
│
├─ cold/
│ ├─ init.py
│ ├─ main.py # 入口：python -m cold 執行
│ ├─ utils.py # clear_screen, 輸入/確認工具
│ │
│ ├─ tools/ # 共用工具函式 (可擴充)
│ │ ├─ init.py
│ │ ├─ file_tools.py # 檔案讀寫/整理
│ │ ├─ system_tools.py # 系統指令、檢查
│ │ ├─ text_tools.py # 文字處理 / 格式化
│ │ ├─ menu_tools.py # 共用選單顯示/導航輔助
│ │ └─ net_tools.py # 網路請求/檢查
│ │
│ ├─ core/ # 共用邏輯
│ │ ├─ init.py
│ │ ├─ settings.py # flags, user_settings 存取
│ │ ├─ state_manager.py # flag 狀態管理
│ │ ├─ menu_engine.py # 共用選單顯示/導航
│ │ ├─ checker.py # 健檢邏輯 (可自動安裝)
│ │ ├─ logger.py # log 存取/匯出
│ │ └─ user.py # 使用者驗證 / profile
│ │
│ ├─ templates/ # 模板
│ │ ├─ menu_template.txt
│ │ └─ confirm_template.txt
│ │
│ ├─ startup/ # 🔌 啟動選單群組
│ │ ├─ init.py
│ │ ├─ start_menu.py # 啟動入口 (顯示啟動 / 關閉)
│ │ ├─ launch.py # ▶️ 啟動邏輯 (檢查 2~5 flag → 顯示開始)
│ │ ├─ device_selection.py # 裝置選擇 (Android / iOS)
│ │ └─ close.py # 關閉
│ │
│ ├─ android/ # Android 專屬流程
│ │ ├─ init.py
│ │ ├─ initial_setup/ # ⚙️ 初始設定流程 (2~5)
│ │ │ ├─ init.py
│ │ │ ├─ init_entry.py
│ │ │ ├─ basic_setup/ # 2️⃣ 基本設定
│ │ │ │ ├─ init.py
│ │ │ │ ├─ basic_setup_menu.py
│ │ │ │ ├─ language/ # 語言設定
│ │ │ │ │ ├─ init.py
│ │ │ │ │ ├─ language_menu.py
│ │ │ │ │ ├─ chinese.py
│ │ │ │ │ └─ english.py
│ │ │ │ ├─ color_scheme/ # 🎨 顏色方案
│ │ │ │ │ ├─ init.py
│ │ │ │ │ ├─ color_menu.py
│ │ │ │ │ ├─ color_categories.py
│ │ │ │ │ ├─ color_details.py
│ │ │ │ │ ├─ color_picker.py
│ │ │ │ │ └─ restore_defaults.py
│ │ │ │ └─ restore_defaults.py
│ │ │ ├─ tutorial/ # 3️⃣ 說明與教學
│ │ │ │ ├─ init.py
│ │ │ │ ├─ tutorial_menu.py
│ │ │ │ ├─ tutorial_content.py
│ │ │ │ └─ tutorial_ack.py
│ │ │ ├─ system_settings/ # 4️⃣ 系統需開啟設定
│ │ │ │ ├─ init.py
│ │ │ │ ├─ system_settings_menu.py
│ │ │ │ ├─ accessibility.py
│ │ │ │ ├─ notification_access.py
│ │ │ │ ├─ battery_optimization.py
│ │ │ │ └─ termux_permissions.py
│ │ │ └─ health_check/ # 5️⃣ 初步系統健檢
│ │ │ ├─ init.py
│ │ │ ├─ health_check_menu.py
│ │ │ ├─ check_python_packages.py
│ │ │ ├─ check_termux_tools.py
│ │ │ ├─ auto_install.py
│ │ │ ├─ skip_handler.py
│ │ │ └─ canxing_override.py
│ │ │
│ │ ├─ bug_report/ # 🐞 錯誤回報
│ │ │ ├─ init.py
│ │ │ ├─ bug_report_menu.py
│ │ │ ├─ submit.py
│ │ │ ├─ drafts.py
│ │ │ └─ stats.py
│ │ └─ start_button.py # ▶️ 開始按鈕
│ │
│ │ ├─ user_mode/ # 👤 使用者模式
│ │ │ ├─ init.py
│ │ │ ├─ user_mode_menu.py # ROOT / NoROOT 選擇
│ │ │ ├─ root/
│ │ │ │ ├─ init.py
│ │ │ │ ├─ root_menu.py
│ │ │ │ ├─ mode_checker.py
│ │ │ │ ├─ unlock/
│ │ │ │ │ ├─ init.py
│ │ │ │ │ ├─ unlock_menu.py
│ │ │ │ │ ├─ unlock_setup.py
│ │ │ │ │ └─ unlock_confirm.py
│ │ │ │ ├─ script_manager/
│ │ │ │ │ ├─ init.py
│ │ │ │ │ ├─ menu.py
│ │ │ │ │ ├─ create.py
│ │ │ │ │ ├─ edit.py
│ │ │ │ │ ├─ schedule.py
│ │ │ │ │ ├─ share.py
│ │ │ │ │ ├─ delete.py
│ │ │ │ │ └─ recycle_bin.py
│ │ │ │ ├─ logs/
│ │ │ │ │ ├─ init.py
│ │ │ │ │ ├─ menu.py
│ │ │ │ │ ├─ view.py
│ │ │ │ │ ├─ search.py
│ │ │ │ │ └─ export.py
│ │ │ │ ├─ personal_settings/
│ │ │ │ │ ├─ init.py
│ │ │ │ │ ├─ menu.py
│ │ │ │ │ ├─ colors.py
│ │ │ │ │ ├─ language.py
│ │ │ │ │ ├─ notifications.py
│ │ │ │ │ └─ restore_defaults.py
│ │ │ │ ├─ teaching/
│ │ │ │ │ ├─ init.py
│ │ │ │ │ ├─ content.py
│ │ │ │ │ └─ ack.py
│ │ │ │ ├─ system_settings/
│ │ │ │ │ ├─ init.py
│ │ │ │ │ ├─ check_accessibility.py
│ │ │ │ │ ├─ check_notifications.py
│ │ │ │ │ ├─ battery_optimization.py
│ │ │ │ │ └─ termux_permissions.py
│ │ │ │ └─ health_check/
│ │ │ │ ├─ init.py
│ │ │ │ ├─ check_packages.py
│ │ │ │ ├─ auto_install.py
│ │ │ │ └─ skip_override.py
│ │ │ └─ no_root/
│ │ │ ├─ init.py
│ │ │ ├─ menu.py
│ │ │ └─ restricted_features.py
│ │
│ └─ storage/ # 使用者專屬資料 / 日誌 / 設定
│ ├─ users/
│ │ ├─ user_<id>/
│ │ │ ├─ profile.json
│ │ │ ├─ settings.json
│ │ │ ├─ logs/
│ │ │ │ ├─ session.log
│ │ │ │ └─ error.log
│ │ │ └─ scripts/
│ │ │ ├─ <script>.py
│ │ │ └─ recycle_bin/
│ │ │ └─ <deleted_script>.py
│ │ └─ ...
│ └─ admin/ # 管理者統計 / 全域日誌
│ ├─ system_stats.json
│ └─ all_logs/
│ └─ <log_file>.log

yaml
複製程式碼

---

## 三、操作與啟動流程

### 1️⃣ 啟動選單

=== Cold 系統 ===
🚀 開始
👤 使用者模式
⚙️ 基本設定
📖 說明與教學
📱 系統需開啟設定
🧪 系統健檢
🚪 離開
🐞 錯誤回報
markdown
複製程式碼

- 使用者必須先完成 2~5 初始設定後才能按「開始」
- 所有重要操作均需二次確認 (Y/N)
- 系統自動保存所有日誌與設定

### 2️⃣ 初始設定流程（2~5）

- **2️⃣ 基本設定**：語言、顏色方案、恢復預設  
- **3️⃣ 說明與教學**：閱讀確認  
- **4️⃣ 系統需開啟設定**：無障礙、通知、電池優化、Termux 權限  
- **5️⃣ 系統健檢**：檢查 Python 套件、Termux 工具，可自動安裝，`canxing` 強制跳過  

### 3️⃣ 使用者模式

- **👑 管理者**
  - 使用者管理、系統維護、腳本管理、統計  
- **👤 普通使用者**
  - ROOT / NoROOT 選擇
  - 腳本管理、日誌查看/匯出、個人設定、教學、系統設定、健檢、離開、錯誤回報  

---

## 四、介面美化規範

- 標題與分隔：`=== 標題 ===`  
- 錯誤訊息：紅色  
- 成功訊息：綠色  
- 提示訊息：黃色  
- 標題文字：青色  
- 所有操作需確認並保存  
- 每次切換畫面自動清空  

---

## 五、日誌與錯誤回報

- 使用者日誌自動上傳，管理者可查看全部  
- 錯誤回報選單：
  - 健檢錯誤 → 自動上傳日誌  
  - 手動回報 → 標題 + 詳細描述 + 是否附加日誌  
- 所有操作會紀錄時間戳  

---

## 六、模組化與擴充

- Cold 核心模組：`core/`, `tools/`, `startup/`, `android/`, `storage/`  
- 工具模組可自由新增 `.py`  
- 選單、設定、教學、日誌均可擴充  
- 支援 PyPI / pip 安裝與更新  

---

## 七、PyPI / pip 發佈規範

- `python -m build` 打包  
- `twine upload dist/*` 上傳  
- `pip install Cold` 或 `pip install --upgrade Cold` 安裝/更新  
- `pyproject.toml` 與 `setup.cfg` 控制元資料  
- `MANIFEST.in` 控制打包檔案  
- `requirements.txt` 列出依賴套件  

---

## 八、Cold 操作規範

1. 任何重要操作需二次確認 (Y/N)  
2. 所有資料與日誌自動保存  
3. 強制跳過關鍵字：`canxing`  
4. ROOT 模式可解鎖手機密碼，NoROOT 提示使用者自行操作  
5. 所有初始設定 2~5 完成後才可按「開始」  
6. 支援自動安裝缺少的套件或提示手動安裝  
7. 日誌保存路徑：`storage/users/<user_id>/logs`  
8. 管理者可查看所有使用者日誌與系統統計  

---

## 九、其他說明

- Cold 專案僅於 Termux 執行  
- 支援 git update、自動保存、PyPI 上傳  
- 介面統一科技感、乾淨整潔  
- 可自由新增腳本、工具模組、選單與教學內容  
- 所有選單與流程可快速擴充  
