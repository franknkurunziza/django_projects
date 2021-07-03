from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('home/<url>',views.home),#<url> to catch anything / after home
    path('redirect/',views.redirected),
    path('complete_redirected/',views.complete),
    path('<path:resources>', views.catch_all)    #<url> to catch anything url box
]
