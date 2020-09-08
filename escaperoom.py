from app import app, socketio

if __name__ == '__main__':
    print('Running...')
    socketio.run(app, debug=True)