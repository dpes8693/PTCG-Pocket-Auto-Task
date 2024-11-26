import os
import shutil

# 定義來源和目標目錄
input_path = r"C:\Users\User\Documents\XuanZhi9\Pictures\Screenshots"
output_path = r"C:\Users\User\Desktop\py\Screenshots"

# 確保目標目錄存在，若不存在則建立
os.makedirs(output_path, exist_ok=True)

# 移動檔案
for file_name in os.listdir(input_path):
    source_file = os.path.join(input_path, file_name)
    destination_file = os.path.join(output_path, file_name)

    # 檢查是否為檔案（不處理子目錄）
    if os.path.isfile(source_file):
        shutil.move(source_file, destination_file)
        print(f"Moved: {source_file} -> {destination_file}")

print("所有檔案已成功搬移!")
