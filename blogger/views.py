from django.shortcuts import render
from django.contrib.auth.models import User


# Create your views here.
def bloggers_list(request):
    users = User.objects.all()
    return render(request, "blogger/bloggers_list.html", {"users": users})