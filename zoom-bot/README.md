# 🔷 Zoom-Bot: Meeting Management System

A database-driven automation project that manages Zoom meeting schedules and automatically joins them using Python. Built for academic demonstration of DBMS concepts with real-world automation using PyAutoGUI and Discord Webhooks.

---

## 📌 Features

- 🗓️ Add, edit, delete scheduled Zoom meetings via web interface
- 🤖 Automatically join Zoom meetings based on stored schedule
- 🎙️ Toggle microphone and camera as per database values
- 📢 Sends join status to Discord via webhook notification
- 🧠 Fully integrated with MySQL for database management

---

## 🛠️ Tech Stack

| Layer        | Technology       |
|--------------|------------------|
| Backend      | Python            |
| Web Server   | Flask             |
| Automation   | PyAutoGUI         |
| Database     | MySQL             |
| Scheduler    | Custom Python loop (every 60s) |
| Notification | Discord Webhooks  |

---

## 🧩 Project Structure

```
zoom-bot/
│
├── app.py                 # Flask web server
├── db.py                  # DB connection and CRUD functions
├── zoom_bot.py            # PyAutoGUI script to join Zoom meetings
├── scheduler.py           # Background script that checks and joins meetings
├── discord_notify.py      # Discord webhook integration
├── templates/             # HTML templates (Jinja2)
│   ├── index.html
│   └── add_meeting.html
├── static/                # (Optional) CSS or JS files
└── README.md              # You're here!
```

---

## 🗃️ Database Schema

### Table: `meetings`

| Field             | Type          | Description                     |
|------------------|---------------|---------------------------------|
| `id`             | INT (PK)      | Unique identifier               |
| `title`          | VARCHAR       | Meeting topic/title             |
| `meeting_id`     | VARCHAR       | Zoom Meeting ID                 |
| `password`       | VARCHAR       | Zoom meeting password           |
| `participant_name` | VARCHAR     | Name to display while joining   |
| `datetime`       | DATETIME      | Scheduled time for the meeting  |
| `mic`            | TINYINT(1)    | Mic on/off (1/0)                |
| `camera`         | TINYINT(1)    | Camera on/off (1/0)             |

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/yourname/zoom-bot.git
cd zoom-bot
```

### 2. Set up a virtual environment (optional but recommended)

```bash
python -m venv zoom_bot_env
zoom_bot_env\Scripts\activate  # On Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure MySQL

- Create a database named `zoom_bot`
- Import the provided schema to create the `meetings` table

### 5. Run the Flask app

```bash
python app.py
```

Visit: `http://localhost:5000/` to open the dashboard.

### 6. Run the scheduler (in another terminal)

```bash
python scheduler.py
```

---

## 💬 Discord Webhook Setup

1. Create a webhook URL from your Discord server settings.
2. Paste it into `discord_notify.py`:

```python
WEBHOOK_URL = "https://discord.com/api/webhooks/..."
```

---

## 📸 Sample Screenshots

- Web Dashboard  
- Add Meeting Form  
- Discord Join Notifications  
- Zoom Auto-Join Console Output  

_(Add them here if available)_

---

## 🧠 Credits

Developed by **Deepu Yadav**  
B.Tech CSE, DYPIU, 2024–25  
Under the guidance of Ms. Shobhana Patil

---

## 📄 License

This project is for educational purposes. Feel free to modify and build on it with credit.

