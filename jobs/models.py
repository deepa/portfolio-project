from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=200)
    detail = models.TextField()
    link = models.CharField(max_length=100)


    def __str__(self):
        return self.title
