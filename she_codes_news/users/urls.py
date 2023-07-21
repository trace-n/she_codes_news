# users/urls.py
from django.urls import path, reverse_lazy 
from .views import DisplayAccountView, CreateAccountView, ChangeAccountView, FavouriteView, AddFavView #ChangePasswordView, 
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    path('<int:pk>/display-account', DisplayAccountView.as_view(), name='viewAccount'),
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    # path('<int:pk>/change-account/', ChangeAccountView.as_view(), name='changeAccount'),
    path('change-account/', ChangeAccountView.as_view(), name='changeAccount'),
    # path('<int:pk>/password/', ChangePasswordView.as_view(), name='changePassword'),  
    path('change-password/', auth_views.PasswordChangeView.as_view(template_name='users/changePassword.html', success_url = reverse_lazy('password_change_done')), name='change-password'),
    # path('change-password', auth_views.Pass Change')  
    path('fav-story/<int:pk>/', AddFavView.as_view(), name='favAdd'),     
    path('favourites/', FavouriteView.as_view(), name='favourites'),    
]
