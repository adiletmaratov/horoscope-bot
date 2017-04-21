from django.test import TestCase
from django.urls import reverse

from bot.request_senders import NambaOneRequestSender


class NambaOneRequestSenderTest(TestCase):
    def test(self):
        url = reverse('horoscopes:index')
        sender = NambaOneRequestSender(url, {})
        response = sender.send_post()
        print(response)
