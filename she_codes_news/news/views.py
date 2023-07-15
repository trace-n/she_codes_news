from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory
from .forms import StoryForm
# from django.views.generic.edit import DeleteView


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
        context['story_categories'] = NewsStory.objects.filter(category__icontains="Science")
        # print(context['story_categories'])
        return context

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

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