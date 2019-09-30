import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.TextField(max_length=5000)
    pub_date = models.DateTimeField(auto_now_add=True)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="choices")
    choice_text = models.TextField()
    votes = models.IntegerField(default=0)
    posted_date = models.DateTimeField(auto_now_add=True)
