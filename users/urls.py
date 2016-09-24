from django.conf.urls import url
from users.views import LoginView, LogoutView, BlogListView, SignUpView

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='user_login'),
    url(r'^signup/$', SignUpView.as_view(), name='user_sign_up'),
    url(r'^logout/$', LogoutView.as_view(), name='user_logout'),
    url(r'^blogs/$', BlogListView.as_view(), name='blog_list')
]
