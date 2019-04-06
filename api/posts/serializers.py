from .models import Post
from rest_framework import serializers


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'contents', 'tags', 'created_at', 'update_at',)
        read_only_fields = ('created_at', 'update_at',)
