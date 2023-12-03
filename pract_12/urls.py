from django.urls import path
from pract_12 import views

pract_12_urls = [
    path('list_book', views.list_books),
    path('create-book', views.create_book),
    path('update-book/<int:id>', views.update_book),
    path("graph", views.graph)
]