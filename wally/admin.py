from django.contrib import admin
from .models import Post,Comment


# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display=("user_name","post")

admin.site.register(Post)
admin.site.register(Comment,CommentAdmin)