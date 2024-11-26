# https://github.com/tesseract-ocr/tesseract/releases/tag/5.5.0
# pip install pytesseract pillow
# pip install tesseract
# pip install tesseract-ocr
import os
from PIL import Image
import pytesseract

# 設定 Tesseract 執行檔路徑（Windows 使用者需手動設定）測試方式:
# "C:\Program Files\Tesseract-OCR\tesseract.exe" --version 
# 設定 Tesseract 執行檔的正確路徑
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def find_first_screenshot(directory):
    """尋找目錄中第一個以 'Screenshot' 開頭的檔案"""
    for filename in sorted(os.listdir(directory)):
        if filename.startswith("Screenshot") and filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            return os.path.join(directory, filename)
    return None

def check_text_in_image(image_path):
    """檢查圖片中是否包含特定文字"""
    try:
        # No cost
        target_text = "no cost"
        # Bonus Pick
        bonus_pick = "bonus pick"
        # Rare Pick
        rare_pick = "rare pick"        
        # 開啟圖片
        img = Image.open(image_path)
        # 使用 OCR 辨識文字
        text = pytesseract.image_to_string(img)
        print(f"圖片的文字有:\n{text}")
        # 判斷文字是否包含目標文字
        if rare_pick in text.lower():
            return 2
        if bonus_pick in text.lower():
            return 1
        return 3
    except Exception as e:
        print(f"Error processing image: {e}")
        return False

# 主程式
if __name__ == "__main__":
    directory = "./Screenshots"  # 圖片所在的資料夾，這裡預設為當前目錄

    # 找到第一張 Screenshot 開頭的圖片
    image_path = find_first_screenshot(directory)

    if image_path:
        print(f"找到圖片檔案: {image_path}")
        mode = check_text_in_image(image_path)
        # 判斷圖片中是否包含目標文字
        if mode == 1:
            print(f"result:免費")
        if mode == 2:
            print(f"result:稀有3費")
        if mode == 3:
            print(f"result:冷卻中")
    else:
        print("未找到 Screenshot 開頭的圖片檔案")
