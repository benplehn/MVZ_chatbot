from django.urls import path
from .views import ChatMessageListCreateView, ChatMessageDetailView, chatbot_view, home, get_last_bot_reply


urlpatterns = [
    path('messages/', ChatMessageListCreateView.as_view(), name = 'message-list-create'),
    path('messages/<int:pk>/', ChatMessageDetailView.as_view(), name = 'message-detail' ),
    path('chatbot/', chatbot_view, name='chatbot'),
    path('', home, name='home'),
    path('chatbot/reply/', get_last_bot_reply, name='get_last_bot_reply'),


]