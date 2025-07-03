from django.db import models
from datetime import datetime
# Create your models here.

class Comment(models.Model):
    user_email = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200)
    comment_date = models.DateTimeField(default= datetime.now ,blank=True)
    post_id = models.IntegerField()
    comment_text = models.TextField()


    def __str__(self):
        return self.comment_text

