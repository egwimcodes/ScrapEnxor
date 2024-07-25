# scraper/urls.py
from django.urls import path
from .views import index, scrape

urlpatterns = [
    path('', index, name='index'),
    path('scrape/', scrape, name='scrape'),
]
