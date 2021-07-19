
from django.urls import path
from .views import *

urlpatterns = [
    path('',home),
    path('dashboard',dashboard),
    path('user/create',create),
    path('user/login',login),
    path('user/log_out',logout),

]