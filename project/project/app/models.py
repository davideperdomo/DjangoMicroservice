# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Team(models.Model):

    MICRO = 'micro'
    FUT5 = 'fut5'
    FUTBOL = 'futbol'

    SPORTS_CHOICES = (
        (MICRO, 'Micro'),
        (FUT5, 'Fut5'),
        (FUTBOL, 'Futbol'),
    )

    name = models.CharField(max_length=50)
    #release_date = models.DateField()
    calification = models.IntegerField(default=0)
    sport = models.CharField(max_length=10, choices=SPORTS_CHOICES)
    captain_id =  models.CharField(max_length=50)