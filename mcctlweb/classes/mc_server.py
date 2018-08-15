# mc_server.py

import subprocess
from threading import Thread
from mcctlweb import socketio


class MCServer(Thread):
    def __init__(self):
        self.sub = subprocess.Popen('java -jar minecraft_server.1.12.2.jar', stdout=subprocess.PIPE,
                                    stdin=subprocess.PIPE)
        super(MCServer, self).__init__()

    def stop_server(self):
        self.sub.stdin.write('stop\n')

    def run(self):
        while True:
            # print(sub.stdout.readline().decode('ascii'))
            socketio.emit('terminal', self.sub.stdout.readline().decode('ascii'), namespace='/terminal')

    def run_command(self, command):
        self.sub.stdin.write(command)

# def start_server():
#     sub = subprocess.Popen('java -jar minecraft_server.1.12.2.jar', stdout=subprocess.PIPE,
#                            stdin=subprocess.PIPE)
#     # time.sleep(10)
#     while True:
#         # print(sub.stdout.readline().decode('ascii'))
#         socketio.emit('terminal', sub.stdout.readline().decode('ascii'), namespace='/terminal')
#
#
# def stop_server():
#     sub.stdin.write('stop\n')
#
#
# def run_command(command):
#     sub.stdin.write(command + '\n')
