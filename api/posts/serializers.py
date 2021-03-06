from .models import Post
from rest_framework import serializers


class PostSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Post
        
        fields = ('id', 'title', 'subtitle', 'slug','contents', 'tag', 'cover_image_url', 'created_at', 'update_at',)
        read_only_fields = ('created_at', 'update_at',)
        