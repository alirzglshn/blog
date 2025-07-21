from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['receiving_blogger' , 'text']


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['text', 'replies_to']
        widgets = {
            'replies_to': forms.HiddenInput()
        }
