from .models import Devlog
from rest_framework import serializers


class DevlogSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Devlog
        
        fields = ('id', 'title', 'subtitle', 'slug','contents', 'tag', 'cover_image_url', 'created_at', 'update_at',)
        read_only_fields = ('created_at', 'update_at',)
        