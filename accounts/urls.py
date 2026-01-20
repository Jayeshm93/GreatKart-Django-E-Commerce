from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    # User verification for active via mail link
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),

]

