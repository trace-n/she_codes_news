from django.shortcuts import render, get_object_or_404
 
# Create your views here.

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views import generic
from .models import CustomUser
from news.models import NewsStory
from .forms import CustomUserCreationForm, CustomUserChangeForm #, CustomUserChangePasswordForm
from django.http import HttpResponseRedirect

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
    
# class ChangePasswordView(UpdateView):
#     model = CustomUser
#     form_class = CustomUserChangePasswordForm
#     # slug_url_kwarg = "username"
#     # slug_field = "username"    
#     success_url = reverse_lazy('news:index')
#     template_name = 'users/changePassword.html'

#     def get_object(self, queryset=None):
#         return self.request.user


def AddFavouriteView(request, pk):
    # model = NewsStory
    # template_name = 'favourites.html'
    # context_object_name = 'fav_stories'
    # check if news story id exist 
    user_fav = get_object_or_404(CustomUser, id=request.user.id)
    
    # check if user exists wtih favourite 
    if user_fav.favourites.filter(id=pk).exists(): 
        user_fav.favourites.remove(pk)
    else: 
        user_fav.favourites.add(pk)
    # 
    # success_url = reverse_lazy('news:index')            
    return HttpResponseRedirect(request.META['HTTP_REFERER'])




def FavouriteView(request):
    # template_name = 'users/favourites.html'
    # context_object_name = 'favourites'
    # user_fav = get_object_or_404(CustomUser, id=request.user.id)    
    # new = user_fav.favourites.filter(author_id=request.user) 
    new = NewsStory.objects.filter(favourited_by=request.user)

    return render(request,'users/favourites.html', { 'fav_stories': new })

