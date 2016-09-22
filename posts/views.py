from django.views.generic import ListView

from posts.models import Post, VISIBILITY_PUBLIC


class HomeView(ListView):

    queryset = Post.objects.all().filter(visibility=VISIBILITY_PUBLIC).order_by('-created_at')
    context_object_name = 'post_list'
    template_name = 'posts/home.html'
