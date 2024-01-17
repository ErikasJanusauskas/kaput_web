from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Quizzes(models.Model):
    name         = models.TextField     ('name')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Quiz'
        verbose_name_plural = 'Quizzes'

class Questions(models.Model):
    quiz         = models.ForeignKey    (Quizzes, blank=True, null=True, on_delete=models.CASCADE, name='quiz')
    name         = models.TextField     ('name')
    answer_1     = models.TextField     ('answer_1')
    answer_2     = models.TextField     ('answer_2')
    answer_3     = models.TextField     ('answer_3')
    answer_4     = models.TextField     ('answer_4')
    answer_r     = models.IntegerField  (validators=[MinValueValidator(1), MaxValueValidator(4)], name="answer_r")
    img_path     = models.TextField     ('img_path')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

