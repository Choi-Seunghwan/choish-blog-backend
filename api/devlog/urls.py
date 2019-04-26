from django.urls import path
from .views import DevlogList, DevlogRetrieveUpdateDestroy, DevlogCreate



urlpatterns = [
    path('', DevlogList.as_view(), name='devlog_list'),
    path('devlog/<slug:slug>/', DevlogRetrieveUpdateDestroy.as_view(), name='devlog_detail'),
    path('new/', DevlogCreate.as_view(), name='devlog_create'),

]

