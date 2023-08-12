from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render

from .models import ChatMessage, ChatSession
from .serializers import ChatMessageSerializer, ChatSessionSerializer
from .chatbot_logic import get_bot_response

from django.http import HttpResponse

# Create your views here.

class ChatMessageListCreateView(generics.ListCreateAPIView):
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializer

class ChatMessageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializer


@api_view(['POST'])
def chatbot_view(request):
    user_message = request.data.get('message', '')
    bot_response = get_bot_response(user_message)

    # Create a new ChatSession first
    chat_session = ChatSession()
    chat_session.save()

    # Now, create ChatMessage instances associated with the chat_session
    ChatMessage.objects.create(session=chat_session, sender=ChatMessage.USER, content=user_message)
    ChatMessage.objects.create(session=chat_session, sender=ChatMessage.BOT, content=bot_response)
    
    return Response({"response": bot_response})


@api_view(['GET'])
def get_last_bot_reply(request):
    last_reply = ChatMessage.objects.filter(sender=ChatMessage.BOT).last()
    if last_reply:
        return Response({"response": last_reply.content})
    return Response({"response": "No reply found."})





def home(request):
    return HttpResponse("Welcome to the Chatbot Project!")