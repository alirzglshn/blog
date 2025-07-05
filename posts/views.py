from django.shortcuts import render
from .models import Post

# Create your views here.
def posts(request):
    posts_list = Post.objects.all()
    context = {
        "posts" : posts_list
    }
    return render(request , "posts/posts.html" , context)

def post(request, post_id:int):
    return render(request , "posts/post.html" , {})

def search(request):
    return render(request , "posts/search.html" , {})


# 00:03 JUly 6 2025