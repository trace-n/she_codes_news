# users/urls.py
from django.urls import path, reverse_lazy 
from .views import DisplayAccountView, CreateAccountView, ChangeAccountView, FavouriteView, AddFavouriteView #ChangePasswordView, 
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    path('<int:pk>/display-account', DisplayAccountView.as_view(), name='viewAccount'),
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    # path('<int:pk>/change-account/', ChangeAccountView.as_view(), name='changeAccount'),
    path('change-account/', ChangeAccountView.as_view(), name='changeAccount'),
    # path('<int:pk>/password/', ChangePasswordView.as_view(), name='changePassword'),  
    path('change-password/', auth_views.PasswordChangeView.as_view(template_name='registration/changePassword.html', success_url = reverse_lazy('users:password_change_done')), name='change-password'),
    path('password_change/done', auth_views.PasswordChangeDoneView.as_view(template_name='registration/passwordDone.html'), name='password_change_done'),
    # path('change-password', auth_views.Pass Change')  
    path('fav-story/<int:pk>/', AddFavouriteView, name='favouriteAdd'),     
    path('favourites/', FavouriteView, name='favourites'),    
]

# class PasswordResetDoneView(PasswordContextMixin, TemplateView):
#     template_name = "registration/password_reset_done.html"
#     title = _("Password reset sent")
