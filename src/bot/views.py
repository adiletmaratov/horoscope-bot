from django.http import JsonResponse
from django.http.response import HttpResponsePermanentRedirect
from django.urls import reverse
from django.views import View

from bot.models import NambaOneUser


class FollowBotView(View):
    def post(self, request, *args, **kwargs):
        user, created = NambaOneUser.objects.get_or_create(
            n1_user_id=request.POST.get('id'),
        )
        return JsonResponse({})


class UnfollowBotView(View):
    def post(self, request, *args, **kwargs):
        return JsonResponse({})


class NewChatView(View):
    def post(self, request, *args, **kwargs):
        return HttpResponsePermanentRedirect(reverse('bot:follow'))

