from django.db import models

# Create your models here.

class Questions(models.Model):
    title = models.CharField('Question', max_length=50)