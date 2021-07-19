
from django.urls import path
from .views import *


urlpatterns = [
    path('courses', course),
    path('create', create)
]