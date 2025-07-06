
from django.shortcuts import render , redirect
from posts.models import Post


# Create your views here.
def index(request):
    posts = Post.objects.order_by('-post_date').filter(is_published = True)[:2]
    return render(request, 'index.html' , {'posts' : posts})

def about(request):
    return render(request , 'about.html' , {})