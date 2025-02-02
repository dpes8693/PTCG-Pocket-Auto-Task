import keyboard
import os
from PIL import Image
import pytesseract
import shutil
import time
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

# 配置
class Config:
    """應用程式配置管理"""
    TESSERACT_PATH = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    # 路徑配置
    SCREENSHOTS_INPUT_PATH = r"C:\Users\YOUR_USER\Documents\XuanZhi9\Pictures\Screenshots"
    SCREENSHOTS_OUTPUT_PATH = r"C:\Users\YOUR_USER\Desktop\py\Screenshots"
    SCREENSHOTS_OK_PATH = r"C:\Users\YOUR_USER\Desktop\py\Screenshots"
    SCREENSHOTS_TEMP_PATH = r"C:\Users\YOUR_USER\Desktop\py\temp"

# 影像辨識
pytesseract.pytesseract.tesseract_cmd = Config.TESSERACT_PATH
# 初始化執行次數
execution_count = 0

def find_first_screenshot(directory):
    """尋找目錄中第一個以 'Screenshot' 開頭的檔案"""
    for filename in sorted(os.listdir(directory)):
        if filename.startswith("Screenshot") and filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            return os.path.join(directory, filename)
    return None

def check_text_in_image(image_path):
    """檢查圖片中是否包含特定文字"""
    try:
        target_text = "no cost"
        bonus_pick = "bonus pick"
        rare_pick = "rare pic"
        date_has_changed = "date has changed"
        # 開啟圖片
        img = Image.open(image_path)
        # 使用 OCR 辨識文字
        text = pytesseract.image_to_string(img)
        print(f"ocr: {text}")
        # print(f"圖片的文字有:\n{text}")
        # 定義來源和目標目錄
        input_path = Config.SCREENSHOTS_OUTPUT_PATH
        output_path = Config.SCREENSHOTS_TEMP_PATH
        move_img(input_path, output_path)

        # 判斷文字是否包含目標文字
        if rare_pick in text.lower():
            return 2
        if bonus_pick in text.lower():
            return 1
        if target_text in text.lower():
            return 1
        if date_has_changed in text.lower():
            return 0
        return 3
    except Exception as e:
        print(f"Error processing image: {e}")
        return False

def open_ld_player():
    """啟動(切換到模擬器)"""
    print(">>切換到模擬器")    
    keyboard.send("alt+tab")

def move_img(input_path, output_path):
    """搬移圖片到正確目錄"""
    # 確保目標目錄存在，若不存在則建立
    os.makedirs(output_path, exist_ok=True)

    # 移動檔案
    for file_name in os.listdir(input_path):
        source_file = os.path.join(input_path, file_name)
        destination_file = os.path.join(output_path, file_name)

        # 檢查是否為檔案（不處理子目錄）
        if os.path.isfile(source_file):
            shutil.move(source_file, destination_file)
            # print(f"Moved: {source_file} -> {destination_file}")

def screen_shot():
    """截圖"""
    print(">>截圖")
    keyboard.send("ctrl+0")

def lt_to_get_card_challenge_flow():
    """回首頁並進入得卡"""
    print(">>回首頁並進入得卡")
    keyboard.send("ctrl+g")

def lt_scroll_down_flow():
    """得卡往下滑動"""
    print(">>得卡往下滑動")
    keyboard.send("ctrl+h")

def lt_choose_card_flow():
    """選卡並抽"""
    print(">>選卡並抽")
    keyboard.send("ctrl+j")

def lt_load_menu():
    """首頁刷新"""
    print(">>首頁刷新")
    keyboard.send("ctrl+k")
    
def lt_date_change():
    """日期更新"""
    print(">>日期更新")
    keyboard.send("ctrl+l")

def auto_task(is_skip_enter_flow):
    global execution_count
    execution_count += 1
    print(f"A程式執行中，目前是第 {execution_count} 次執行")    
    if is_skip_enter_flow == False:
        lt_load_menu()
        time.sleep(30)
        lt_to_get_card_challenge_flow()
        time.sleep(15)
    screen_shot()
    # 等幾秒 避免檔案沒儲存
    time.sleep(10)
    # 定義來源和目標目錄
    input_path = Config.SCREENSHOTS_INPUT_PATH
    output_path = Config.SCREENSHOTS_OUTPUT_PATH 
    move_img(input_path, output_path)
    # 圖片所在的資料夾，這裡預設為當前目錄
    directory = "./Screenshots"  

    # 找到第一張 Screenshot 開頭的圖片
    image_path = find_first_screenshot(directory)

    if image_path:
        print(f"找到圖片檔案: {image_path}")
        mode = check_text_in_image(image_path)
        # 判斷圖片中是否包含目標文字
        if mode == 1:
            print(f"🆓免費")
            lt_choose_card_flow()
            time.sleep(29)
            screen_shot()
            time.sleep(5)
            # 將成果截圖存到ok
            input_path = Config.SCREENSHOTS_INPUT_PATH
            output_path = Config.SCREENSHOTS_OK_PATH
            move_img(input_path, output_path)
            time.sleep(10)
            print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        if mode == 2:
            print(f"💎稀有挑戰")
            lt_scroll_down_flow()
            time.sleep(10)
            auto_task(True)
        if mode == 3:
            print(f"🕛冷卻中")
        if mode == 0:
            lt_date_change()
    else:
        print("💥例外情況 沒找到圖片")

def get_card_task():
    auto_task(False)

# 主程式
if __name__ == "__main__":
    print("⛳抽卡啟動!", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    open_ld_player()
    time.sleep(3)
    # 建立排程器
    scheduler = BlockingScheduler()
    # 每 x 分鐘執行一次 容忍 10 秒的延遲
    scheduler.add_job(get_card_task, 'interval', minutes=15, misfire_grace_time=10)
    # 開始排程
    try:
        print("第一次執行")
        auto_task(False)
        print("排程已開始")
        scheduler.start()

    except (KeyboardInterrupt, SystemExit):
        print("排程已停止")