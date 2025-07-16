from django.urls import path
from . import views

urlpatterns = [
    path('' , views.posts , name = 'posts') ,
    path('<int:post_id>' , views.post , name = 'post') ,
    path('search' , views.search , name = 'search'),
    path('post/<int:post_id>/like/', views.like_post, name='like_post'),
    path('new_post' , views.new_post , name = 'new_post'),
    ]

