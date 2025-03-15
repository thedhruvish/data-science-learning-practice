from django.urls import path
from .views import about,show

urlpatterns = [
    path('',about),
    path('a/',about),
    path('show/',show)
]