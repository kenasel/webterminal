# -*- coding: utf-8 -*-

from channels.generic.websocket import WebsocketConsumer
from channels.generic.websocket import AsyncWebsocketConsumer

import paramiko
import threading
import time
import json

# 配置服务器信息
HOSTS = "192.168.14.250"
PORT = 22
USERNAME = "root"
PASSWORD = "3Ger_3Ger"

# 线程类
class MyThread(threading.Thread):
    def __init__(self, id, chan):
        threading.Thread.__init__(self)
        self.chan = chan

    def run(self):
        while not self.chan.chan.exit_status_ready():
            time.sleep(0.1)
            try:
                data = self.chan.chan.recv(1024)
                self.chan.send(data.decode('utf-8'))
            except Exception as ex:
                print(str(ex))
        self.chan.sshclient.close()
        return False


# websocket处理类--同步
class MyConsumer(WebsocketConsumer):

    def connect(self):
        # Called on connection. Either call
        self.accept()
        
        hosts = self.scope["url_route"]["kwargs"]["hosts"]
        port = self.scope["url_route"]["kwargs"]["port"]
        username = self.scope["url_route"]["kwargs"]["username"]
        password = self.scope["url_route"]["kwargs"]["password"]

        self.sshclient = paramiko.SSHClient()
        self.sshclient.load_system_host_keys()
        self.sshclient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.sshclient.connect(hosts, port, username, password)
        self.chan = self.sshclient.invoke_shell(term='xterm')
        self.chan.settimeout(0)
        t1 = MyThread(999, self)
        t1.setDaemon(True)
        t1.start()

    def receive(self, text_data=None, bytes_data=None):     
        self.chan.send(text_data)
       

    def disconnect(self, close_code):
        # Called when the socket closes
        self.sshclient.close()
        self.close()


# websocket处理类--异步
class MyAsyncConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        # Called on connection. Either call
        await self.accept()

        self.sshclient = paramiko.SSHClient()
        self.sshclient.load_system_host_keys()
        self.sshclient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.sshclient.connect(HOSTS, PORT, USERNAME, PASSWORD)
        self.chan = self.sshclient.invoke_shell(term='xterm')
        self.chan.settimeout(0)
        t1 = MyThread(999, self)
        t1.setDaemon(True)
        t1.start()

    async def receive(self, text_data=None, bytes_data=None):     
        await self.chan.send(text_data)
       

    def disconnect(self, close_code):
        # Called when the socket closes
        self.sshclient.close()
        self.close()