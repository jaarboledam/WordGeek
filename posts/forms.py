from posts.models import Post
from django.forms import ModelForm


class PostCreationForm(ModelForm):

    class Meta:
        model = Post
        exclude = ['owner']