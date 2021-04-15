from django.db import models
import os

class Translate(models.Model):
  text = models.TextField(max_length=1000)
  translated_text = models.TextField(max_length=1000)