from django.urls import path
from . import views

urlpatterns = [
    path("", views.login, name="Log In"),
    path("catalogue/", views.catalogue, name="Catalogue"),
    path("pet/", views.petmain, name="Pet"),
    path("adoption/", views.adoption, name="Adoption"),
]
