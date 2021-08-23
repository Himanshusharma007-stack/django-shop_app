from django.contrib import admin
from django.urls import path
from BLC import views

urlpatterns = [
    path('', views.index, name= 'home'),
    path('about/', views.about, name= 'about'),
    path('contact/', views.contact, name= 'contactUs'),
    path('tracker/', views.tracker, name= 'tracker'),
    path('search/', views.search, name= 'search'),
    path("products/<int:myid>", views.productView, name= 'ProductView'),
    path('checkout/', views.checkout, name= 'checkout'),
]
