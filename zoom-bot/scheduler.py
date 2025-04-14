
import time
from datetime import datetime, timedelta
from db import get_all_meetings
from zoom_bot import join_meeting_by_id

def check_and_join_meetings():
    print("🔁 Checking for meetings to join...")
    all_meetings = get_all_meetings()
    now = datetime.now()
    window = timedelta(minutes=5)  # +/- 1 minute window

    for meeting in all_meetings:
        meeting_time = meeting['datetime']
        if meeting_time and abs(meeting_time - now) <= window:
            print(f"🕒 Joining meeting: {meeting['title']} ({meeting['meeting_id']})")
            join_meeting_by_id(meeting['id'])

if __name__ == "__main__":
    print("🔧 Zoom-Bot Scheduler started.")
    while True:
        check_and_join_meetings()
        time.sleep(60)  # Check every 60 seconds
