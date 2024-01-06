from datetime import datetime, timedelta
import time

def get_nearest_multiple_of_3():
    current_minute = datetime.utcnow().minute
    nearest_multiple = (current_minute // 15) * 15
    return nearest_multiple

def utc_countdown_nearest_multiple_of_3(duration_minutes=15):
    while True:
        nearest_multiple = get_nearest_multiple_of_3()
        target_time = datetime.utcnow().replace(second=0, microsecond=0, minute=nearest_multiple) + timedelta(minutes=duration_minutes)
        max_duration = datetime.utcnow() + timedelta(minutes=60)
        if duration_minutes > 60:
            duration_minutes = 60
        remaining_time = min(target_time, max_duration) - datetime.utcnow()
        remaining_seconds = int(max(remaining_time.total_seconds(), 0))
        # counter_data = {"counter": (remaining_seconds-2)}
        print(remaining_time,end='\r')
        time.sleep(1)

utc_countdown_nearest_multiple_of_3()        