from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.HomeClass.as_view(), name='home'),
    path('create/', views.CreateClass.as_view(), name='create'),
    path('home/<int:pk>/', views.DetailClass.as_view(), name='detail'),
    path('post/', views.PostClass.as_view(), name='post'),
]