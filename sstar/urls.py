from django.contrib import admin
from django.urls import path
from.import views
from .views import insurance

urlpatterns = [
    path('' ,views.home, name='home'),

    path ('about/', views.about, name='about' ),

    path('application/', views.application, name='application'),

    path('portfolio/', views.portfolio, name='portfolio'),

    path('services/', views.services, name='services'),

    path('login/', views.login_user, name='login'),

    path('logout/', views.logout_user, name='logout'),

    path('register/', views.register_user, name='register'),

    path('insurance/<int:pk>', views.insurance, name='insurance'),

    path ('contact/', views.contact, name='contact'),
]