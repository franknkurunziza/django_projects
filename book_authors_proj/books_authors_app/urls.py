
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add_book',views.add_book),
    path('book/<int:book_id>',views.one_book),
    path('add_author',views.add_author),
    path('author',views.author),
    path('author/<int:author_id>',views.one_author),
    path('author/add_book_author',views.add_book_author),
    path('create_author',views.create_author),
    path('author/<int:author_id>/delete',views.delete_author),

]