from django.urls import path
from .views import ChatMessageListCreateView, ChatMessageDetailView


urlpatterns = [
    path('messages/', ChatMessageListCreateView.as_view(), name = 'message-list-create'),
    path('messages/<int:pk>/', ChatMessageDetailview.as_view(), name = 'message-detail' ),
]