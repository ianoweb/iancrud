from django.urls import path
from django.contrib import admin
from . import views as user_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('signup/', auth_views.LogoutView.as_view(template_name='signup.html'), name='signup'),
]