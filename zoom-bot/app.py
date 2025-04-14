
from flask import Flask, render_template, request, redirect, url_for
from db import get_all_meetings, add_meeting, get_meeting_by_id, update_meeting, delete_meeting
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    meetings = get_all_meetings()
    return render_template('index.html', meetings=meetings)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        data = {
            'title': request.form['title'],
            'meeting_id': request.form['meeting_id'],
            'password': request.form['password'],
            'participant_name': request.form['participant_name'],
            'datetime': request.form['datetime'],
            'mic': 'mic' in request.form,
            'camera': 'camera' in request.form
        }
        add_meeting(data)
        return redirect(url_for('index'))
    return render_template('add_meeting.html')

@app.route('/edit/<int:meeting_id>', methods=['GET', 'POST'])
def edit(meeting_id):
    meeting = get_meeting_by_id(meeting_id)
    if request.method == 'POST':
        data = {
            'title': request.form['title'],
            'meeting_id': request.form['meeting_id'],
            'password': request.form['password'],
            'participant_name': request.form['participant_name'],
            'datetime': request.form['datetime'],
            'mic': 'mic' in request.form,
            'camera': 'camera' in request.form
        }
        update_meeting(meeting_id, data)
        return redirect(url_for('index'))
    return render_template('add_meeting.html', meeting=meeting)

@app.route('/delete/<int:meeting_id>')
def delete(meeting_id):
    delete_meeting(meeting_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
