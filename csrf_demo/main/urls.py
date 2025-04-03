from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login),
    path('write/', views.write_post),
    path('attack/', views.csrf_attack),
]