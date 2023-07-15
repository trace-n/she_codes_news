# users/urls.py
from django.urls import path 
from .views import CreateAccountView, ChangeAccountView

app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    # path('<int:pk>/change-account/', ChangeAccountView.as_view(), name='changeAccount'),
    path('change-account/', ChangeAccountView.as_view(), name='changeAccount'),
]
