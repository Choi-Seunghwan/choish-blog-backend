from django.urls import path
from .views import PostList, PostRetrieveUpdateDestroy



urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('post/<slug:slug>/', PostRetrieveUpdateDestroy.as_view(), name='post_detail'),
]

