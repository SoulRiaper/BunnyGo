from django.urls import path 
from . import views

urlpatterns = [
    path("<int:articleNumber>/<str:articleText>/", views.get_one_article),
    path("", views.index, name = "main"),
    path("Long/", views.get_articles),
    path("json/", views.get_article_as_json)
]
