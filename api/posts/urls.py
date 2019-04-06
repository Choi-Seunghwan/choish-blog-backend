from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PostViewSet

post_list = PostViewSet.as_view({
    'post': 'create',
    'get': 'list'
})

post_detail = PostViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = format_suffix_patterns([
    path('', post_list, name='post_list'),
    path('<int:pk>/', post_detail, name='post_detail'),
])

