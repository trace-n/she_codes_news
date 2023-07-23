from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    path('add-story/', views.AddStoryView.as_view(), name='newStory'),
    path('<int:pk>/edit-story/', views.EditStoryView.as_view(), name='editStory'),
    path('<int:pk>/delete-story/', views.DeleteStoryView.as_view(), name='deleteStory'),
    path('search-results/', views.SearchResultsView.as_view(), name='searchresults'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('<str:category>', views.CategoryView.as_view(), name='category'),    
   
]

