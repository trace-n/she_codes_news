from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views import generic
from .models import CustomUser
from news.models import NewsStory
from .forms import CustomUserCreationForm, CustomUserChangeForm

class DisplayAccountView(generic.ListView):
    model = CustomUser
    success_url = reverse_lazy('news:index')
    template_name = 'users/viewAccount.html'


class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

class ChangeAccountView(UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    # slug_url_kwarg = "username"
    # slug_field = "username"    
    success_url = reverse_lazy('news:index')
    template_name = 'users/changeAccount.html'

    def get_object(self, queryset=None):
        return self.request.user
    
class AddFavView(CreateView):
    model = NewsStory
    template_name = 'news/favouriteStory.html'
    context_object_name = 'fav_stories'
    # news = get_object_or_404(NewsStory, id=id)
    # author = request.user
    # remove or add favourites for user
    # if NewsStory.favourites.filter(id=self.request.user).exists(): 
    #     NewsStory.favourites.remove(self.request.user)
    # else: 
    #     NewsStory.favourites.remove(self.request.user)

    success_url = reverse_lazy('news:index')    

class FavouriteView(generic.ListView):
    model = CustomUser
    template_name = 'users/favourites.html'
    context_object_name = 'favourites'
    # new = NewsStory.favourites.filter(id=request.user)
    # return render(request,'favourites/html', { 'new': new })