# chatbot > models.py

from django.db import models
from accounts.models import CustomUser

class Conversation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    prompt = models.CharField(max_length=512)
    response = models.TextField()

    def __str__(self):
        return f"{self.prompt}: {self.response}"