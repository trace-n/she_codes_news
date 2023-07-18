# users/urls.py
from django.urls import path 
from .views import DisplayAccountView, CreateAccountView, ChangeAccountView, FavouriteView, AddFavView

app_name = 'users'

urlpatterns = [
    path('<int:pk>/display-account', DisplayAccountView.as_view(), name='viewAccount'),
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    # path('<int:pk>/change-account/', ChangeAccountView.as_view(), name='changeAccount'),
    path('change-account/', ChangeAccountView.as_view(), name='changeAccount'),
    path('fav-story/<int:pk>/', AddFavView.as_view(), name='favAdd'),     
    path('favourites/', FavouriteView.as_view(), name='favourites'),    
]
