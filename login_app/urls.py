from django.urls import path, include
from . import views


urlpatterns = [
    path('signup/', views.SignUpClass.as_view(), name='signup'),
    path('top/', views.index, name='login_index'),
    path('', include('django.contrib.auth.urls')),
]