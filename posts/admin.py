from django.contrib import admin
from blogger.models import Blogger
from .models import Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('id' ,'title' ,'blogger' ,'comments_count','likes_count','post_date','is_published',)
    list_display_links = [ 'id' , 'title']
    list_editable = ['is_published']
    list_filter = ['blogger']
    search_fields = ['title' , 'text' , 'blogger__name']
    readonly_fields = ['comments_count' , 'likes_count' , 'blogger']
    list_per_page = 20

    def save_model(self, request, obj, form, change):
        obj.blogger = Blogger.objects.filter(user=request.user).first()
        return super().save_model(request , obj , form , change)

    def get_queryset(self, request):
        qs = super(PostAdmin , self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        else :
            return qs.filter(blogger__user = request.user)
admin.site.register(Post , PostAdmin)
