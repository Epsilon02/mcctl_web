# mc_server.py

import subprocess
from threading import Thread
import pexpect

from mcctlweb import socketio


class mcServer(Thread):
    def __init__(self):
        self.server_mc = pexpect
        self.child: pexpect.spawn = None
        super(mcServer, self).__init__()

    def run(self):
        self.child = self.server_mc.spawn('java -jar minecraft_server.1.12.2.jar')
        while True:
            # print(sub.stdout.readline().decode('ascii'))
            socketio.emit('terminal', self.child.readline(), namespace='/terminal')

    def stop_server(self):
        # self.server_mc.expect('*')
        self.child.send('stop')

    def run_command(self, command):
        # self.server_mc.expect('*')
        self.child.send(command)


class MCServer(Thread):
    def __init__(self):
        self.sub: subprocess.Popen = None
        super(MCServer, self).__init__()

    def stop_server(self):
        print('stopped')
        self.sub.stdin.write(b'stop\n')
        self.sub.stdin.close()

    def run(self):
        self.sub = subprocess.Popen('java -jar minecraft_server.1.12.2.jar', stdout=subprocess.PIPE,
                                    stdin=subprocess.PIPE)
        while True:
            # print(sub.stdout.readline().decode('ascii'))
            socketio.emit('terminal', self.sub.stdout.readline().decode('ascii'), namespace='/terminal')

    def run_command(self, command: str):
        self.sub.stdin.write(str.encode(command))
        self.sub.stdin.close()

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
