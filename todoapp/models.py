from datetime import datetime

from django.db import models


# Create your models here.
class ToDo(models.Model):
    content = models.CharField(max_length=500, blank=False, null=False)
    date_posted = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.content[0:10]
