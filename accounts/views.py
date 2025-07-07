from django.shortcuts import render , redirect
from django.contrib import messages
# Create your views here.

# sign in
def sign_in(request):
    if request.method == 'POST':
        return redirect('sign_in')
    else:
        return render(request, 'accounts/sign_in.html', {})

# sin up
def sign_up(request):
    if request.method == 'POST':
        messages.error(request , "this is a test for error message")
        return redirect('sign_up')
    else:
        return render(request, 'accounts/sign_up.html', {})


# sign out
def sign_out(request):
    if request.method == 'POST':
        return redirect('sign_out')
    else:
        return render(request, 'accounts/sign_out.html', {})

