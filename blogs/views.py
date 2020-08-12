from django.shortcuts import render
from .models import BlogPost
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import BlogForm

# Create your views here.

def index(request):
	"""The Home Page for Log"""
	blogs = BlogPost.objects.order_by('date_added')
	context = {'blogs': blogs}
	return render(request, 'blogs/index.html', context)
	
def blog(request, blog_id):
	"""Show a single topic and all its entries."""
	blog = BlogPost.objects.get(id=blog_id)
	context = {'blog': blog}
	return render(request, 'blogs/blog.html', context)
	
def new_blog(request):
	if request.method != 'POST':
		form = BlogForm()
	else:
		form = BlogForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('blogs:index'))
	context = {'form' : form}
	return render(request, 'blogs/new_blog.html', context)
				
		
