from django.contrib import admin
from .models import Blogger
# Register your models here.
class BloggerAdmin(admin.ModelAdmin):
    list_display = ('id' ,'name','photo','birth_date','register_date','posts_count','description','email','phone',)
    list_display_links = [ 'id' , 'name' , 'email']
    search_fields = ['name' , 'email' , 'phone']
    readonly_fields = ['posts_count']
    list_per_page = 10
admin.site.register(Blogger , BloggerAdmin)