import pyautogui
import time
import subprocess
import pygetwindow as gw
from db import get_meeting_by_id
from discord_notify import send_meeting_status

ZOOM_PATH = "C:\\Users\\dy068\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"

# These must be verified using pyautogui.position()
JOIN_BUTTON_XY = (800, 420)
NAME_FIELD_XY = (770, 530)
MIC_TOGGLE_XY = (900, 605)
CAMERA_TOGGLE_XY = (1010, 605)

def wait(seconds=2):
    time.sleep(seconds)

def open_zoom():
    subprocess.Popen(ZOOM_PATH)
    wait(5)

def focus_zoom():
    try:
        zoom = [w for w in gw.getWindowsWithTitle("Zoom") if w.isVisible][0]
        zoom.activate()
        wait(1)
    except Exception as e:
        print("⚠️ Could not focus Zoom window:", e)

def write(text):
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')
    pyautogui.write(text)
    wait()

def join_meeting(meeting_id, password, participant_name, mic, camera):
    open_zoom()

    focus_zoom()
    pyautogui.click(*JOIN_BUTTON_XY)
    wait()

    # Enter meeting ID
    pyautogui.click(771,461)
    wait()
    write(meeting_id)
    wait()

    # Enter participant name
    pyautogui.moveTo(*NAME_FIELD_XY)
    pyautogui.click(*NAME_FIELD_XY)
    wait()
    write(participant_name)
    wait()
    pyautogui.press('enter')
    wait()
    

    # Toggle mic & camera based on DB (0 = Off, 1 = On)
    if mic == 0:
        pyautogui.click(*MIC_TOGGLE_XY)
        wait()
    if camera == 1:
        pyautogui.click(*CAMERA_TOGGLE_XY)
        wait()

    pyautogui.press('enter')
    wait()

    # Enter password if needed
    if password:
        write(password)
        pyautogui.press('enter')
        wait()

    print("✅ Meeting join attempt completed.")

def join_meeting_by_id(meeting_id):
    meeting = get_meeting_by_id(meeting_id)
    if meeting:
        try:
            join_meeting(
                meeting['meeting_id'],
                meeting['password'],
                meeting['participant_name'],
                mic=meeting['mic'],
                camera=meeting['camera']
            )
            send_meeting_status(meeting, status="Joined successfully ✅")
        except Exception as e:
            send_meeting_status(meeting, status=f"Failed to join ❌ ({str(e)})")
    else:
        print("❌ Meeting not found.")
