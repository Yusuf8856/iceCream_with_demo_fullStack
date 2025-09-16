from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name="home"),  # It gives the index page if url is blank('').
    path("about/", views.about, name="about"),  #It gives the about page.
    path("contact/", views.contact, name="contact"), #It gives the contact page.
    path("services/", views.services, name="services"),
    path("cake/", views.cake, name="cake"),
    path("softy/", views.softy, name="softy"), 
    path("iceCream/", views.iceCream, name="iceCream"), 


]