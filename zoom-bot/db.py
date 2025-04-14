
import mysql.connector
from datetime import datetime

# Database connection config
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'zoom_bot'
}

def connect_db():
    return mysql.connector.connect(**DB_CONFIG)

# CRUD Operations

def add_meeting(data):
    conn = connect_db()
    cursor = conn.cursor()
    query = """INSERT INTO meetings (title, meeting_id, password, participant_name, datetime, mic, camera, follow_up_meeting_id)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""

    values = (
    data['title'], data['meeting_id'], data['password'],
    data['participant_name'], data['datetime'],
    data['mic'], data['camera'], data.get('follow_up_meeting_id')
    )

    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()

def get_all_meetings():
    conn = connect_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM meetings ORDER BY datetime ASC")
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results

def get_meeting_by_id(meeting_id):
    conn = connect_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM meetings WHERE id = %s", (meeting_id,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def update_meeting(meeting_id, data):
    conn = connect_db()
    cursor = conn.cursor()
    query = """UPDATE meetings SET title=%s, meeting_id=%s, password=%s, participant_name=%s,
               datetime=%s, mic=%s, camera=%s WHERE id=%s"""
    values = (
        data['title'], data['meeting_id'], data['password'],
        data['participant_name'], data['datetime'],
        data['mic'], data['camera'], meeting_id
    )
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()

def delete_meeting(meeting_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM meetings WHERE id = %s", (meeting_id,))
    conn.commit()
    cursor.close()
    conn.close()
