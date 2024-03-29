from django.db import models
from django.contrib.auth.models import User
from quiz.models import Questions
# Create your models here.
class Profile(models.Model):
    user        = models.ForeignKey     (User, on_delete=models.CASCADE)
    question    = models.ForeignKey     (Questions, blank=True, null=True, on_delete=models.CASCADE)
    answer      = models.IntegerField   (null=True, blank=True)
    isMarked    = models.BooleanField   (default=False)
    time        = models.DateTimeField  (auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.question.name} ({self.time.strftime('%d/%m/%Y')})"