import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin

class Question(models.Model):
    question_text = models.CharField(max_length=200, default="Default Question Text")
    pub_date = models.DateTimeField("date published", default=timezone.now)

    def __str__(self):
        return self.question_text

    
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    # def was_published_recently(self):
    #    now = timezone.now()
    # # Check if the publication date is in the future
    #    if self.pub_date > now:
    #      return False
    # # Check if the publication date is within the last 24 hours
    #    return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, default=1)
    choice_text = models.CharField(max_length=200, default="Default Choice Text")
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text
