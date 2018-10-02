# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# Create your models here.

## Mongo
from mongoengine import Document, fields

class Equipo(Document):
    nombre = fields.StringField(required=True)
    deporte = fields.StringField(required=True)
    capitan_un = fields.StringField(required=True)
    value = fields.DynamicField(required=True)
    ##miembros = fields.ListField(fields.StringField())
##end Mongo
