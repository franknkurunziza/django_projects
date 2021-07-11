
from django.urls import path
from . import views

urlpatterns = [
    path('all',views.shows),
    path('all/<int:id>',views.one_show),
    path('all/<int:id>/edit',views.edit_page),
    path('update/<int:id>',views.update),
    path('all/<int:id>/destroy',views.delete),
    path('new',views.add_shows),
    path('create',views.create),
]
