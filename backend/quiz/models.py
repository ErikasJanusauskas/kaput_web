from django.db import models

# Create your models here.

class Questions(models.Model):
    title   = models.CharField('Question', max_length=512),
    anwer_1 = models.CharField('Answer_1', max_legth=128 ),
    anwer_2 = models.CharField('Answer_2', max_legth=128 ),
    anwer_3 = models.CharField('Answer_3', max_legth=128 ),
    anwer_4 = models.CharField('Answer_4', max_legth=128 ),
    notes   = models.CharField('Notes'   , max_legth=128 ),
    picyure = models.CharField('Image'   , max_length=256)