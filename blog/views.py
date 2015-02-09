from django.shortcuts import render
from blog.models import Post

def index(request):
	return render(request,'blog/home.html')

def post(request, post_id=1):
	post = Post.objects.get(pk=post_id)

	# Defining context
	context = {}
	context['post'] = post

	return render(request, 'blog/post.html', context)