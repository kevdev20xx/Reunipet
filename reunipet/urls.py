from django.urls import path
from django.contrib.auth import views as auth_views
from reunipet import views



urlpatterns = [
    path('sign-up/', views.sign_up, name='sign-up'),
    path('login/', auth_views.LoginView.as_view(template_name='reunipet/login.html'), name='login')
]