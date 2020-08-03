from flask import render_template
from app import app, socketio
from flask_socketio import join_room, emit, send

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/hint/')
def show_hint():
    return render_template('hint_screen.html')
    
@socketio.on('hint')
def send_hint(data):
    hint = data['hint']
    emit('hint', hint, broadcast=True)