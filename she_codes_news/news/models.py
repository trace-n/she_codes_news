from django.db import models
from django.contrib.auth import get_user_model

# class NewsCategory(models.Model):
#     category = models.CharField(max_length=50)

class NewsStory(models.Model):

    CATEGORY_CHOICES = (
        ('World', 'World'),
        ('Business', 'Business'),
        ('Sport', 'Sport'),
        ('Science', 'Science'),
        ('Entertainment', 'Entertainment'),
    )
    
    title = models.CharField(max_length=200)
    # author = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    # pub_date = models.DateTimeField(default=timezone.now)
    pub_date = models.DateTimeField(auto_now_add=True) # set the creation date automatically when object created
    change_date = models.DateTimeField(auto_now=True) # set the field to now when record is saved
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='World')
    # category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=200, default = 'placeholder-3.jpg')
    content = models.TextField()
    favourites = models.ManyToManyField(get_user_model(), related_name='favourite', default=None, blank=True)

# class FavStory(models.Model):
#     author = models.ForeignKey(
#         get_user_model(),
#         on_delete=models.CASCADE
#     )
#     story = models.ForeignKey(
#         NewsStory,
#         on_delete=models.CASCADE
#     )

