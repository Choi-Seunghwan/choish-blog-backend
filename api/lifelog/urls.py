from django.urls import path
from .views import LifelogList, LifelogRetrieveUpdateDestroy, LifelogCreate



urlpatterns = [
    path('', LifelogList.as_view(), name='lifelog_list'),
    path('lifelog/<slug:slug>/', LifelogRetrieveUpdateDestroy.as_view(), name='lifelog_detail'),
    path('new/', LifelogCreate.as_view(), name='lifelog_create'),

]

