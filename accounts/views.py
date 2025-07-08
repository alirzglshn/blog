from django.shortcuts import render , redirect
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth import authenticate , login , logout
# Create your views here.

# sign in
def sign_in(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            messages.success(request, ("You have been logged in successfully"))
            return redirect('index')
        else:
            messages.success(request, ("Login failed , Please try again."))
            return redirect('sign_in')
    else:
        return render(request, 'accounts/sign_in.html', {})


# sin up
def sign_up(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have been registered successfully")
                return redirect("index")
            else:
                messages.error(request, "Registration succeeded, but login failed.")
                return redirect("sign_in")
        else:
            messages.error(request, "Registration failed, please try again.")
            return redirect("sign_up")
    else:
        return render(request, 'accounts/sign_up.html', {'form' : form})


# sign out
def sign_out(request):
    logout(request)
    messages.success(request, ("You have been signed out successfully"))
    return redirect('index')

