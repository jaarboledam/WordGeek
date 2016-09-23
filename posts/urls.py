from django.conf.urls import url

from posts.views import PostCreationView, PostDetailView

urlpatterns = [
    url(r'^new-post/$', PostCreationView.as_view(), name='post_creation'),
    url(r'^blogs/(?P<username>\w+)/(?P<pk>\d+)$', PostDetailView.as_view(), name='post_detail'),
]
