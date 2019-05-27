from .serializers import LifelogSerializer
from .models import Lifelog
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.


class LifelogList(ListAPIView):
    queryset = Lifelog.objects.all().order_by('-created_at')
    serializer_class = LifelogSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('id', 'title','tag', 'slug' )
    
class LifelogRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Lifelog.objects.all()
    serializer_class = LifelogSerializer
    lookup_field = 'slug'

class LifelogCreate(CreateAPIView):
    queryset = Lifelog.objects.all()
    serializer_class = LifelogSerializer
