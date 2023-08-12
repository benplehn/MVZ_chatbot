from rest_framework import generics

from .models import ChatMessage, ChatSession
from .serializers import ChatMessageSerializers, ChatSessionSerializers

# Create your views here.

class ChatMessageListCreateView(generics.ListCreateAPIView):
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializer

class ChatMessageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializer



