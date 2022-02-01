from django.db import models

class Word(models.Model):
    wordname = models.CharField(max_length=15)
    content = models.CharField(max_length=100)

    def __str__(self):
        return self.wordname
