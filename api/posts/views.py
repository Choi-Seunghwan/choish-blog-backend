from .serializers import PostSerializer
from .models import Post
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.


class PostList(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('id', 'title','tag', 'slug' )
    

class PostRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'


class PostCreate(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def preform_create(self, serializer):
        print("When load???")