from flask import render_template, request, Blueprint
from mcctlweb import app
from mcctlweb import socketio
from flask_socketio import send
from mcctlweb.classes.rand import RandomThread
from mcctlweb.classes.terminal import Terminal
import json
import time

server_stat_id = 1

terminal_thread = Terminal()
terminal_thread.do_run = False

netdata_server = "http://localhost:19999/"


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.jinja2', server_stat=server_stat_id, title="Terminal")


@app.route("/about")
def about():
    return render_template('about.jinja2', server_stat=server_stat_id, title="About")


@app.route("/grid")
def grid():
    return render_template('home.jinja2', server_stat=server_stat_id, netdata_server=netdata_server)


@app.route("/start", methods=['GET'])
def start():
    data = {'key': 'Starting Server'}
    if not terminal_thread.is_alive():
        terminal_thread.start()
    time.sleep(1)
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route("/stop", methods=['GET'])
def stop():
    data = {'key': 'Server stopped!'}
    id = 1
    if terminal_thread.is_alive():
        terminal_thread.stop()
        terminal_thread.join()
    print(terminal_thread.is_alive())
    time.sleep(1)
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route("/restart", methods=['GET'])
def restart():
    data = {'key': 'restart'}
    time.sleep(1)
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response


@app.errorhandler(404)
def page_not_found(error):
    return "Something went wrong (-_-)"


@socketio.on('message')
def handle_message(message):
    print('received message:' + message)
    send(message, broadcast=True)


@socketio.on('connect', namespace='/random-number')
def random_number():
    global thread

    thread = RandomThread()
    # thread.start()
