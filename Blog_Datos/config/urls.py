from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Agregar estas dos líneas para login y logout
    path('accounts/login/', auth_views.LoginView.as_view(template_name='AppCoder/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='inicio'), name='logout'),

    path('', include('AppCoder.urls')),
]
