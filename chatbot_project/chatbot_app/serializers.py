from rest_framework import serializers
from .models import ChatMessage, ChatSession

class ChatMessageSerializers(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = '__all__'

class ChatSessionSerializers(serializers.ModelSerializer):
    class Meta:
        model = ChatSession
        fiels = '__all__'
        