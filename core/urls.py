from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('category/',category,name='category'),
    path('register/',register,name='register')
]