import threading

import requests

from django.conf import settings


class NambaOneRequestSender(object):
    def __init__(self, url, data):
        self._url = url
        self._data = data
        self._headers = {'X-Namba-Auth-Token': settings.API_TOKEN}

    def send_post(self):
        requests.post(self._url, self._data, headers=self._headers)


class CreateChat(threading.Thread):
    def __init__(self, user_id):
        super(CreateChat, self).__init__()
        self._user_id = user_id

    def run(self):
        self.create()

    def create(self):
        chat_create_url = settings.API_SERVICE_URL + "chats/create"
        data = {}
        request_sender = NambaOneRequestSender(chat_create_url, data)
        response = request_sender.send_post()
