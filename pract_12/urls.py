from django.urls import path
from pract_12 import views

pract_12_urls = [
    path("gen_graph/", views.gen_graph)
]