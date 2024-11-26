import time
from datetime import datetime

# 印出當前時間
current_time = datetime.now()
print("現在時間:", current_time.strftime("%Y-%m-%d %H:%M:%S"))

# 等待 10 秒
time.sleep(10)

# 再次印出時間
later_time = datetime.now()
print("10 秒後時間:", later_time.strftime("%Y-%m-%d %H:%M:%S"))
