from . import views
from django.urls import path, re_path

app_name = "blogs"

urlpatterns = [
path('', views.index, name='index'),
re_path(r'^blogs/(?P<blog_id>\d+)/$', views.blog, name='blog'),
path('new_blog/', views.new_blog, name='new_blog'),
re_path(r'^edit_blog/(?P<blog_id>\d+)/$', views.edit_blog, name='edit_blog'),
]

