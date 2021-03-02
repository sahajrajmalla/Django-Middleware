from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('', views.home),
    # path('excep/', views.excep),
    path('user/', views.user_info),

]