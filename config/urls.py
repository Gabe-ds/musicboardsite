from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # login_app/urls.pyのnameと揃える
    path('login-app/', include('login_app.urls')),
    path('musicboard/', include('musicboard.urls')),
]
