from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello, name='myapp_hello'),  # Home page
    path('', views.MyView.as_view(), name='myapp_myview'),  # MyView page
    path('posts/', views.posts_list, name='myapp_posts_list'),  # Posts list page
]