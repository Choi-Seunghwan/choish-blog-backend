from django.urls import path, re_path
from .views import PostList, PostRetrieveUpdateDestroy, PostCreate



urlpatterns = [
    re_path(r'^$', PostList.as_view(), name='post_list'),
    path('post/<slug:slug>/', PostRetrieveUpdateDestroy.as_view(), name='post_detail'),
    path('new/', PostCreate.as_view(), name='post_create'),

]

