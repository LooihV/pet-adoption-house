from django.urls import path
from . import views

urlpatterns = [
    path("login", views.login_view, name="login"),
    path("home", views.home, name="Home"),
    path("catalogue", views.catalogue, name="Catalogue"),
    path("pet", views.petmain, name="Pet"),
    path("adoption", views.adoption, name="Adoption"),
]
