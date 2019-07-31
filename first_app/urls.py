from django.urls import path
from . import views


urlpatterns = [
    path('<int:abc>/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('newblog/', views.blogpost, name='newblog'),


    path('delete/<int:abc>/', views.delete, name='delete'),
    path('update/<int:abc>/', views.update, name='update'),

]