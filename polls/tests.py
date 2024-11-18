# polls/tests.py
from django.test import TestCase
from .models import Question
import datetime
from django.utils import timezone
from django.core.cache import cache

class MyTests(TestCase):
    def setUp(self):
        # Clear cache before each test
        cache.clear()

    def test_example(self):
        # Your test code here
        pass

class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        print("Future Question pub_date: ", future_question.pub_date)
        print("Current time (timezone.now()): ", timezone.now())
        self.assertIs(future_question.was_published_recently(), False)

    # def test_was_published_recently_with_past_question(self):
    #     """
    #     was_published_recently() returns False for questions whose pub_date
    #     was more than a day ago.
    #     """
    #     time = timezone.now() - datetime.timedelta(days=2)
    #     past_question = Question(pub_date=time)
    #     self.assertIs(past_question.was_published_recently(), False)

    # def test_was_published_recently_with_recent_question(self):
    #     """
    #     was_published_recently() returns True for questions whose pub_date
    #     is within the last day.
    #     """
    #     time = timezone.now() - datetime.timedelta(hours=1)
    #     recent_question = Question(pub_date=time)
    #     self.assertIs(recent_question.was_published_recently(), True)

