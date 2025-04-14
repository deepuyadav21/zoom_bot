import requests
from datetime import datetime

WEBHOOK_URL = "https://discord.com/api/webhooks/1359484506255654983/unHWIf0yo0UHOp-lkD-T221OHU5s-WBMQHT87MwRC6V-hD6eAw1KVRjTeQrjIvWxT6U4"

def send_meeting_status(meeting, status="Joined successfully ✅"):
    time_now = datetime.now().strftime("%Y-%m-%d %I:%M %p")
    message = f"""📢 **Zoom-Bot Meeting Update**

🔹 **Title:** {meeting['title']}
🔹 **Meeting ID:** {meeting['meeting_id']}
👤 **Participant:** {meeting['participant_name']}
📅 **Scheduled Time:** {meeting['datetime']}
🕓 **Joined At:** {time_now}
🎤 **Mic:** {"On" if meeting['mic'] else "Off"}
📷 **Camera:** {"On" if meeting['camera'] else "Off"}

✅ **Status:** {status}
"""
    data = {"content": message}
    response = requests.post(WEBHOOK_URL, json=data)

    if response.status_code == 204:
        print("✅ Notification sent.")
    else:
        print(f"❌ Notification failed. Code: {response.status_code}")
