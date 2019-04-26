from .serializers import DevlogSerializer
from .models import Devlog
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.


class DevlogList(ListAPIView):
    queryset = Devlog.objects.all().order_by('-created_at')
    serializer_class = DevlogSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('id', 'title','tag', 'slug' )
    
class DevlogRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Devlog.objects.all()
    serializer_class = DevlogSerializer
    lookup_field = 'slug'

class DevlogCreate(CreateAPIView):
    queryset = Devlog.objects.all()
    serializer_class = DevlogSerializer
