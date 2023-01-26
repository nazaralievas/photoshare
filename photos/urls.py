from django.urls import path
from .views import *


urlpatterns = [
    path('', gallery, name='gallery'),
    path('photo/<str:pk>/', photoView, name='photo'),
    path('add/', addPhoto, name='add'),
]
