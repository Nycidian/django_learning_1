from django.views.generic import ListView, DetailView

from .models import Post
# Create your views here.

class PublishPostMixin(object):
    def get_queryset(self):
        return self.model.objects.live()

class PostListView(PublishPostMixin, ListView):
    model = Post

    

class PostDetailView(PublishPostMixin, DetailView):
    model = Post
