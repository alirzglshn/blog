from django.shortcuts import render , redirect
from .models import Message
from user_messages.forms import MessageForm


# Create your views here.


def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            the_message = form.save(commit=False)
            the_message.sending_blogger = request.user
            the_message.save()
            return redirect('bloggers_list')
    else :
        form = MessageForm()
    return render(request, 'send_message.html', {'form': form})

def inbox(request):
    messages = Message.objects.filter(receiving_blogger=request.user).order_by('-time')
    return render(request, 'inbox.html', {'messages': messages})