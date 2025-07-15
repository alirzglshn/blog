from allauth.socialaccount.providers.dummy.views import authenticate
from django.shortcuts import render , get_object_or_404 , redirect
from .models import Post
from django.core.paginator import Paginator
from django.db.models import Q
from comments.models import Comment
from comments.forms import The_Comments
# Create your views here.
def posts(request):
    posts_list = Post.objects.order_by('-post_date').filter(is_published = True)
    paginator = Paginator(posts_list , 3)
    page = request.GET.get('page')
    paged_post_list = paginator.get_page(page)
    context = {
        "posts" : paged_post_list
    }
    return render(request , "posts/posts.html" , context)

def post(request, post_id:int):
    post = get_object_or_404(Post , pk=post_id)
    comments = Comment.objects.filter(post=post)
    form = The_Comments()

    if request.method == 'POST':
        form = The_Comments(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            post.comments_count += 1
            post.save()
            return redirect('post', post_id=post_id)

    return render(request , "posts/post.html" , {'post' : post , 'comments' : comments , 'form' : form})

def search(request):
    posts = Post.objects.order_by('-post_date').filter(is_published=True)
    if 'search_text' in request.GET:
        search_text = request.GET['search_text']
        if search_text:
            posts = posts.filter(Q(title__icontains = search_text) | Q(text__icontains = search_text) | Q(blogger__name__icontains = search_text))
    return render(request , "posts/search.html" , {'posts' : posts})


def like_post(request , post_id):
    if not request.user.is_authenticated:
        return render(request , 'accounts/authentication_alert.html' , {})

    post = get_object_or_404(Post , pk=post_id)
    blogger = request.user.blogger
    if blogger in post.likers.all():
        post.likers.remove(blogger)
        post.likes_count -= 1

    else :
        post.likes_count += 1


    post.save()

    return redirect('post' , post_id=post_id)



