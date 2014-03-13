from django.views.generic import ListView, DetailView

from .models import Post
# Create your views here.

class PublishPostMixin(object):
    def get_queryset(self):
        queryset = super(PublishPostMixin, self).get_queryset()
        return queryset.filter(published=True)

class PostListView(PublishPostMixin, ListView):
    model = Post

    

class PostDetailView(PublishPostMixin, DetailView):
    model = Post
