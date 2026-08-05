from django.urls import path
from django.contrib.auth import views as auth_views
from reunipet import views



urlpatterns = [
    path('sign-up/', views.sign_up, name='sign-up'),
    path('login/', auth_views.LoginView.as_view(template_name='reunipet/login.html'), name='login'),
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path("report/", views.report, name='report'),
    path("account_settings/", views.report, name='account_settings'),
    path("your_lost_pets_list/", views.report, name='your_lost_pets_list'),
    path("logout/", auth_views.LogoutView.as_view(next_page="home"), name='logout'),
    
]