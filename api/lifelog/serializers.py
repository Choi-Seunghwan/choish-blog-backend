from .models import Lifelog
from rest_framework import serializers


class LifelogSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Lifelog
        
        fields = ('id', 'title', 'subtitle', 'slug','contents', 'tag', 'cover_image_url', 'created_at', 'update_at',)
        read_only_fields = ('created_at', 'update_at',)
        