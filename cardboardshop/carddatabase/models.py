from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class CardInfo(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=50)
    frameType = models.CharField(max_length=50)
    desc = models.TextField()
    race = models.CharField(max_length=50)
    archetype = models.CharField(max_length=50, null=True, blank=True)
    attribute = models.CharField(max_length=50, null=True, blank=True)
    level = models.PositiveIntegerField(null=True, blank=True)
    linkval = models.PositiveIntegerField(null=True, blank=True)
    linkmarkers = models.CharField(max_length=255, null=True, blank=True)
    attack = models.IntegerField(null=True, blank=True)
    defense = models.IntegerField(null=True, blank=True)
    card_sets = models.JSONField(null=True, blank=True)
    card_images = models.JSONField(null=True, blank=True)
    card_prices = models.JSONField(null=True, blank=True)
    updated_date = models.DateTimeField(default=timezone.datetime(1995, 1, 1))

