from django.db import models

class Word(models.Model):
    wordname = models.CharField(max_length=30)
    content = models.CharField(max_length=1000)
    genre = models.CharField(max_length=30,default='')

    def __str__(self):
        return self.wordname
