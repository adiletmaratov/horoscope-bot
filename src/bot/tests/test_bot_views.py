from django.test import TestCase, RequestFactory
from django.urls import reverse

from bot.models import NambaOneUser
from bot.views import FollowBotView, UnfollowBotView, NewChatView


class FollowBotViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.data = {
            'id': 1,
            'name': 'user name',
            'phone': 'user phone number',
            'gender': 'F',
            'birthdate': '01/01/2000',
            'is_online': 'true',
            'avatar': 'some url'
        }
        self.request = self.factory.post(reverse('bot:follow'), data=self.data)

    def test_view_returns_200_status(self):
        response = FollowBotView.as_view()(self.request)
        self.assertEqual(response.status_code, 200)

    def test_user_is_saved_to_db(self):
        FollowBotView.as_view()(self.request)
        self.assertTrue(NambaOneUser.objects.exists())


class UnfollowBotViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.data = {
            'id': 1,
            'name': 'user name',
            'phone': 'user phone number',
            'gender': 'F',
            'birthdate': '01/01/2000',
            'is_online': 'true',
            'avatar': 'some url'
        }
        self.request = self.factory.post(reverse('bot:unfollow'), data=self.data)

    def test_view_returns_200_status(self):
        response = UnfollowBotView.as_view()(self.request)
        self.assertEqual(response.status_code, 200)


class NewChatViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.data = {
            'id': 1,
            'name': 'user name',
            'phone': 'user phone number',
            'gender': 'F',
            'birthdate': '01/01/2000',
            'is_online': 'true',
            'avatar': 'some url'
        }
        self.request = self.factory.post(reverse('bot:new_chat'), data=self.data)

    def test_view_should_redirect_to_follow_view(self):
        response = NewChatView.as_view()(self.request)
        self.assertEqual(response.status_code, 301)
