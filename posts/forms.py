from django import forms
from .models import Post

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text' , 'title' , 'main_photo' , 'photo_1', 'photo_2', 'photo_3', 'photo_4', 'photo_5', 'photo_6']
        labels = {
            'text' : 'بنویسید...' ,
            'title': 'عنوان',
            'main_photo': 'عکس اصلی (اجباری)',
            'photo_1': 'عکس اول (اختیاری)',
            'photo_2': 'عکس دوم (اختیاری)',
            'photo_3': 'عکس سوم (اختیاری)',
            'photo_4': 'عکس چهارم (اختیاری)',
            'photo_5': 'عکس پنجم (اختیاری)',
            'photo_6': 'عکس ششم (اختیاری)',
        }
