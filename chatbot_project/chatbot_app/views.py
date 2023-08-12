from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view


from .models import ChatMessage, ChatSession
from .serializers import ChatMessageSerializer, ChatSessionSerializer

from .chatbot_logic import get_bot_response

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
    ChatMessage.objects.create(sender=ChatMessage.USER, content=user_message)
    ChatMessage.objects.create(sender=ChatMessage.BOT, content=bot_response)

    return Response({"response": bot_response})
