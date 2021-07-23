
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('dashboard',views.dashboard),
    path('user/create', views.create),
    path('user/login', views.login),
    path('user/log_out', views.logout),
    path('wish_form', views.wish),
    path('new_wish', views.add_wish),
    path('<int:id>/delete', views.delete),
    path('<int:id>/edit', views.edit_page),
    path('edit/<int:id>', views.update),
    path('<int:id>/grant', views.granting),
    path('<int:id>/like', views.like),

]