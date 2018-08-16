# routes.py

import time

from flask import render_template, Blueprint, jsonify
from flask_socketio import send
from mcctlweb import socketio

from mcctlweb.classes.mc_server import MCServer, mcServer

main = Blueprint('main', __name__)

server_stat_id = 1
netdata_server = "http://localhost:19999/"
# server = mcServer()


@main.route('/')
@main.route('/home')
def home():
    return render_template('home.jinja2', netdata_server=netdata_server, server_stat=server_stat_id)


@main.route('/about')
def about():
    return render_template('about.jinja2', title='About')


@main.route("/start", methods=['GET'])
def start():
    data = {'key': 'Starting Server'}
    # server.start()
    # if not terminal_thread.is_alive():
    #     terminal_thread.start()
    time.sleep(1)
    return jsonify(data)


@main.route("/stop", methods=['GET'])
def stop():
    data = {'key': 'Server stopped!'}
    # server.stop_server()
    id = 1
    # if terminal_thread.is_alive():
    #     terminal_thread.stop()
    #     terminal_thread.join()
    # print(terminal_thread.is_alive())
    time.sleep(1)

    return jsonify(data)


@main.route("/restart", methods=['GET'])
def restart():
    data = {'key': 'restart'}
    time.sleep(1)

    return jsonify(data)


@socketio.on('message')
def handle_message(message):
    print('Received message: ' + message)
    # server.run_command(message)
    send(message, broadcast=True)


@socketio.on('terminal')
def handle_terminal(command):
    print(command)
    # server.run_command(command)
