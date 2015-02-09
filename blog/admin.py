from django.contrib import admin
from blog.models import *
from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(SummernoteModelAdmin):
	model = Post

admin.site.register(Post, PostAdmin)
admin.site.register(Category)