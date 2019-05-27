from django.urls import path, include


urlpatterns = [
    path('', include('rest_framework.urls', namespace='rest_framework')),
    path('posts/', include('api.posts.urls')),
    path('devlogs/', include('api.devlog.urls')),
    path('lifelogs/', include('api.lifelog.urls')),
]
