from django.urls import path
from . import views

urlpatterns = [
    path("login", views.login_view, name="login"),
    path("register", views.register_view, name="register"),
    path("home", views.home, name="home"),
    path("catalogue", views.catalogue, name="catalogue"),
    path("pet", views.petmain, name="pet"),
    path("adoption", views.adoption, name="adoption"),
]
