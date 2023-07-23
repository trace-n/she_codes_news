from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory
from .forms import StoryForm
from django.db.models import Q
# from django.views.generic.edit import DeleteView
# from http import 

class IndexView(generic.ListView):
    template_name = 'news/index.html'
    context_object_name = "all_stories"

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all().order_by('pub_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # print(context)
        # print(NewsStory.objects.all())
        context['latest_stories'] = NewsStory.objects.all().order_by('-pub_date')[:4]
        context['category_choices'] = NewsStory.CATEGORY_CHOICES
        # context['story_categories'] = NewsStory.objects.filter(category__icontains="Science")
        # context['categories'] = NewsStory.objects.filter(category="Science")
        return context
    
class CategoryView(generic.ListView):
    model = NewsStory
    template_name = 'news/science.html'  
    context_object_name = 'story_categories'

    def get_queryset(self, category):
        return NewsStory.objects.filter(category=category)

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'
 
 

    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        print(context)
        fav = bool

        if context['story'].favourited_by.filter(id=request.user.id).exists():
            context['favourites'] = True

        return self.render_to_response(context)

    

class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyform'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class EditStoryView(generic.UpdateView):
    model = NewsStory
    form_class = StoryForm
    context_object_name = 'storyform'
    template_name = 'news/editStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)    
    
class DeleteStoryView(generic.DeleteView):
    model = NewsStory    
    # form_class = StoryForm
    context_object_name = 'storyform'
    template_name = 'news/deleteStory.html'
    success_url = reverse_lazy('news:index')

class SearchView(generic.TemplateView):
    template_name = 'news/search.html'

class SearchResultsView(generic.ListView):
    model = NewsStory
    template_name = 'news/searchResults.html'
    context_object_name = 'search_stories' 
    success_url = reverse_lazy('news:index')       

    def get_queryset(self):
        '''Return news stories filtered by author first or last name or category'''
        query_author = self.request.GET.get("author")                
        query_category = self.request.GET.get("category")
        print(query_author, query_category)
        if query_author is None or query_author == "":
            result_set = NewsStory.objects.filter(Q(category__icontains=query_category))

        elif query_category is None or query_category == "": 
            result_set = NewsStory.objects.filter(Q(author__last_name__icontains=query_author) | Q(author__first_name__icontains=query_author))
        else:                                      
            result_set = NewsStory.objects.filter((Q(author__last_name__icontains=query_author) | Q(author__first_name__icontains=query_author)) 
                                        & Q(category__icontains=query_category))
        
        # return NewsStory.objects.filter(Q(author__last_name__icontains=query_author) | Q(author__first_name__icontains=query_author) 
                                        # | Q(category__icontains=query_category))
        return result_set