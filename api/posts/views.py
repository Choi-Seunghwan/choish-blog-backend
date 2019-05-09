from .serializers import PostSerializer
from .models import Post
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny

# Create your views here.


#temp
# from rest_framework.response import Response
# from rest_framework import status
#/temp


class PostList(ListAPIView):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('id', 'title','tag', 'slug' )
    

class PostRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'
    

@permission_classes((IsAuthenticated, )) 
class PostCreate(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # def post(self, request, format=None):
    #     print("Post !!!!!")
    #     serializer = self.serializer_class(data = request.data)
    #     print(request.data)
    #     return Response( status=status.HTTP_200_OK)
