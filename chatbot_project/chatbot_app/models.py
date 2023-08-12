from django.db import models

# Create your models here.

class ChatMessage(models.Model):
    USER = 'USER'
    BOT = 'BOT'
    SENDER_CHOICES = [
        (USER, 'User'),
        (BOT, 'Bot')
    ]
    
    sender = models.CharField(max_length = 4, choices = SENDER_CHOICES, default = USER)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    session = models.ForeignKey('ChatSession', on_delete=models.CASCADE, related_name='message')


class ChatSession(models.Model):
    
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
