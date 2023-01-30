from django.urls import path
from . import views

#URLConfig
urlpatterns = [
    path("", views.index, name='index'),
    path("hello/", views.response, name='response'),
]