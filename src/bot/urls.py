from django.conf.urls import url

from .views import FollowBotView, UnfollowBotView, NewChatView

urlpatterns = [
    url(r'user/follow', FollowBotView.as_view(), name='follow'),
    url(r'user/unfollow', UnfollowBotView.as_view(), name='unfollow'),
    url(r'new/chat', NewChatView.as_view(), name='new_chat'),
]

