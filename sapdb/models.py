import uuid
from django.db import models

# Create your models here.
class Food(models.Model):
    TIER_CHOICES = [
      (1, 'Tier 1'),
      (2, 'Tier 2'),
      (3, 'Tier 3'),
      (4, 'Tier 4'),
      (5, 'Tier 5'),
      (6, 'Tier 6'),
    ]
    tier = models.IntegerField(choices=TIER_CHOICES, default=0)
    name = models.CharField(primary_key=True, max_length=255)
    image = models.CharField(max_length=255)
    effect = models.CharField(max_length=255)
    triggers = models.ManyToManyField('Trigger', related_name='food_triggers')
    packs = models.ManyToManyField('Pack', related_name='food_packs')

class Trigger(models.Model):
    name = models.CharField(primary_key=True, max_length=255)
    type = models.CharField(max_length=255)
    foods = models.ManyToManyField('Food', related_name="trigger_foods")

class Pack(models.Model):
    name = models.CharField(primary_key=True, max_length=255)
    image = models.CharField(max_length=255)
    foods = models.ManyToManyField('Food', related_name='pack_foods')