"""URL configuration for the store app."""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.storehome, name='storehome'),
    path('productinfo/<int:pk>', views.productinfo, name='productinfo'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('reviews/', views.reviews, name='reviews'),
]
