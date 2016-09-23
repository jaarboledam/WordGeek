from django.conf.urls import url
from users.views import LoginView, LogoutView, BlogsListView

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='user_login'),
    url(r'^signup/$', LoginView.as_view(), name='user_signup'),
    url(r'^logout/$', LogoutView.as_view(), name='user_logout'),
    url(r'^blogs/$', BlogsListView.as_view(), name='blog_list')
]
