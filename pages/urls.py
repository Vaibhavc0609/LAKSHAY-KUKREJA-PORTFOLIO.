from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
  path('podcast/', views.podcasts, name='podcasts'),
    path('blog/', views.Blog, name='blog'),
    path('blog/create/', views.blog_create, name='blog_create'),
     path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
     path('blog/delete/<int:pk>/', views.blog_delete, name='blog_delete'),
    path('collaborate/', views.collaborate, name='collaborate'),
]