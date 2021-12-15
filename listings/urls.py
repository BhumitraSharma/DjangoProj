from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='listings'),
    path('listings', views.listing, name='listing'),
    path('search', views.search, name='search')
]