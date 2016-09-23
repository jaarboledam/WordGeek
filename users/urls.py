from django.conf.urls import url
from users.views import LoginView, LogoutView

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='user_login'),
    url(r'^signup/$', LoginView.as_view(), name='user_signup'),
    url(r'^logout/$', LogoutView.as_view(), name='user_logout'),
]
