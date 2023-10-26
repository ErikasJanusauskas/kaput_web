from django.db import models

# Create your models here.

class Questions(models.Model):
    title        = models.CharField('Question', max_length=512)
    answer_1     = models.CharField('Answer_1', max_length=128 )
    answer_2     = models.CharField('Answer_2', max_length=128 )
    answer_3     = models.CharField('Answer_3', max_length=128 )
    answer_4     = models.CharField('Answer_4', max_length=128 )
    answer_right = models.IntegerField()
    notes        = models.CharField('Notes'   , max_length=128 )
    picture      = models.CharField('Image'   , max_length=256)