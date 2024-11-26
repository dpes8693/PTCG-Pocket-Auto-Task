# pip install apscheduler
# pip show apscheduler

from apscheduler.schedulers.blocking import BlockingScheduler

# 初始化執行次數
execution_count = 0

# 定時任務函數
def job():
    global execution_count
    execution_count += 1
    print(f"A程式執行中，目前是第 {execution_count} 次執行")

# 建立排程器
scheduler = BlockingScheduler()

# 每 30 分鐘執行一次
scheduler.add_job(job, 'interval', minutes=1)

# 開始排程
print("排程已啟動，每隔30分鐘執行一次")
try:
    scheduler.start()
except (KeyboardInterrupt, SystemExit):
    print("排程已停止")
