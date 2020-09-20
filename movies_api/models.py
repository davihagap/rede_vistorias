from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=50)
    episode_id = models.IntegerField()
    opening_crawl = models.TextField()
    director = models.CharField(max_length=50)
    producer = models.CharField(max_length=50)
    release_date = models.DateField()
    
    class Meta:
        db_table='movie'
    
class Sequence(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        db_table='sequence'
    
class PositionInOrder(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    sequence = models.ForeignKey(Sequence, on_delete=models.CASCADE)
    position = models.IntegerField()
    
    class Meta:
        db_table='movie_sequence'