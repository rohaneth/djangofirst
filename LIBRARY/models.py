from django.db import models


class books(models.Model):
    book_name = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)
    
class movies(models.Model):
    movie_name = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)

# Create your models here.
