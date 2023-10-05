from django.db import models

class Message(models.Model):
    support_chat = models.ForeignKey(SupportChat, on_delete=models.CASCADE)
    sender = models.CharField(max_length=100)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
