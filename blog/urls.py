from django.urls import path, include
from . import views
from django.contrib import admin
urlpatterns = [
    path('',views.index,name='index'),
    path('allblogs/', views.BlogListView.as_view(), name='allblogs'),
    path('blog/<int:pk>', views.BlogDetailView.as_view(), name='blog-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
]
