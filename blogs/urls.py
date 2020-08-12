from . import views
from django.urls import path

app_name = "blogs"

urlpatterns = [
path('', views.index, name='index'),
path('blogs/(?P<blog_id>\d+)/', views.blog, name='blog'),
path('new_blog/', views.new_blog, name='new_blog'),
path('edit_blog/(?P<blog_id>\d+)/', views.edit_blog, name='edit_blog'),
]
