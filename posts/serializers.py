from rest_framework import serializers
from posts.models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        read_only_fields = ("owner",)


class PostListSerializer(PostSerializer):

    class Meta(PostSerializer.Meta):
        fields = ("id", "title", "intro", "media_url", "publicate_at",)

