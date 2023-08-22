from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('detail/<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('delete/<int:blog_id>/', views.blog_delete, name='blog_delete'),
    path('update/<int:blog_id>/', views.blog_update, name='blog_update'),
    path('create/', views.blog_create, name='blog_create'),
]
