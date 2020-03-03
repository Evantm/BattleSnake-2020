from flask import Flask, jsonify
from snakes import left_snake

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/start')
def start():
    return left_snake.start()


@app.route('/move')
def move():
    return left_snake.move_left()


@app.route('/end')
def end():
    return 'Goodbye!'


@app.route('/ping')
def ping():
    return 'pong'


if __name__ == '__main__':
	app.run()