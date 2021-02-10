from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('blog/<init:blog_id>', blog.views.detail, name='detail'),
    path('blog/new/', blog.views.new, name='new'),
    path('blog/create', blog.views.create, name='create'),
]