import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200, default="Default Question Text")  # Add default value
    pub_date = models.DateTimeField("date published", default=timezone.now)
    
    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, default=1)
    choice_text = models.CharField(max_length=200, default="Default Choice Text")
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text