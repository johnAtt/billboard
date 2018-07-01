from django.db import models
import time

date_created = time.strftime("%Y/%m/%d")

class Quote(models.Model):
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    author = models.CharField(max_length=1000)
    date_post = models.CharField(max_length=1000, default=date_created)

    def __str__(self):
        return self.title + " " + self.description + " " + self.author + " " + self.date_post