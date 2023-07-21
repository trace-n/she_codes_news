from django.db import models 
# from news.models import NewsStory

# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    
    favourites = models.ManyToManyField('news.NewsStory', related_name='favourited_by', default=None, blank=True)

    def __str__(self):
        return self.username