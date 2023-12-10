from django.urls import path
from . import views
from .views import court_list, court_detail

urlpatterns = [
    path('places/', views.place_list, name='place_list'),
    path('court/', views.court_list, name='court_list'),
    path('court/<int:court_id>/', court_detail, name='court_detail'),
]