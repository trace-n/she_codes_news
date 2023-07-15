from django import forms
from django.forms import ModelForm 
from .models import NewsStory

class StoryForm(ModelForm):
    class Meta:
        model = NewsStory

        # fields = ['title', 'author', 'category', 'image_url', 'content']
        fields = ['title', 'category', 'image_url', 'content']
        # widget = forms.Select(choices=CATEGORY_CHOICES),
        
        # fields = ['title', 'author', 'pub_date', 'content']

        # widgets = {
        #     'pub_date': forms.DateInput(
        #         format='%m/%d/%Y',
        #         attrs={
        #             'class':'form-control',
        #             'placeholder':'Select a date',
        #             'type':'date'
        #         }
        #     ),
        # }