from django.urls import path
from . import views

urlpatterns = [
    path('bloggers_list' , views.bloggers_list , name = "bloggers_list" )
]