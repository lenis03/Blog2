from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home_page'),
    path('detail/<int:blog_id>/', views.detail, name='detail'),
    path('delete/<int:blog_id>/', views.delete, name='delete'),
    path('create/', views.create, name='create'),
]
