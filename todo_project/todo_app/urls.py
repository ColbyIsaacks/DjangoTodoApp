from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('deleteItem/<int:id>/', views.deleteItem),
]