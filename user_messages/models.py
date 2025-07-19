from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


User = get_user_model()

class Message(models.Model):
    sending_blogger = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiving_blogger = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    text = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f'Message from {self.sending_blogger} to {self.receiving_blogger}'
