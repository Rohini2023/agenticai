from services.reminder_scheduler import start_scheduler
import time

print("🚀 Scheduler Service Running...")

start_scheduler()

while True:
    time.sleep(10)