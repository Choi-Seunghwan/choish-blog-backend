from .serializers import PostSerializer
from .models import Post
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

#temp
from rest_framework.response import Response
from rest_framework import status
#/temp


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
        print("When loading this line???")

    def post(self, request, format=None):
        print("Post !!!!!")
        serializer = self.serializer_class(data = request.data)
        
        # if serializer.is_valid():
        #     print(request.data)
        # print(request.data)

        # file_obj = request.FILES['myblob']
        # print(file_obj)
        print(request.data)
        return Response( status=status.HTTP_200_OK)
        
        # return Response(request.data, status=status.HTTP_400_BAD_REQUEST)

        