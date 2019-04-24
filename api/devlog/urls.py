from django.urls import path
from .views import DevlogList
# ,DevlogRetrieveUpdateDestroy, DevlogCreate



urlpatterns = [
    path('', DevlogList.as_view(), name='devlog_list'),
    # path('devlog/<slug:slug>/', PostRetrieveUpdateDestroy.as_view(), name='post_detail'),
    # path('new/', PostCreate.as_view(), name='post_create'),

]

