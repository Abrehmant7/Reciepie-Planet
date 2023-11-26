from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_name = models.CharField(max_length=50)
    activity_desc = models.TextField()
    date = models.DateTimeField(default='', null=True)

    def __str__(self) -> str:
        return str (self.activity_name)
