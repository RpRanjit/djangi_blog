from django.urls import path
from . import views

urlpatterns = [
    path('signin/', views.signin_view, name='sign_in'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
   
]