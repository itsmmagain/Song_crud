from email.policy import default
from django.db import models
from datetime import datetime
# Create your models here.
class Artiste(models.Model):
    First_name = models.CharField(max_length=200)
    Last_name = models.CharField(max_length=200)
    Age = models.IntegerField()


    def __str__(self):
        return self.First_name

class Song(models.Model):
    Title = models.CharField(max_length=200)
    Release_date = models.DateField(default=datetime.today)
    Likes = models.IntegerField()
    Artiste_id = models.ForeignKey(Artiste, on_delete=models.PROTECT)


    def __str__(self):
        return self.Title
    
class Lyric(models.Model):
    Lyric = models.CharField(max_length=40)
    Content = models.TextField()
    Song_id = models.ForeignKey(Song, on_delete=models.PROTECT)


    def __str__(self):
        return self.Lyric