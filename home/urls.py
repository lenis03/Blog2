from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home_page'),
    path('detail/<int:todo_id>/', views.detail, name='detail'),
    path('delete/<int:todo_id>/', views.delete, name='delete'),
]
