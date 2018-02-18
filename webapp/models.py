# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.




from mongoengine import *

class Lonely(Document):
    cleverbot = StringField(max_length=200)
