from django.urls import path
from listings import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.list, name='list'),
    path('search', views.search, name='search'),
]