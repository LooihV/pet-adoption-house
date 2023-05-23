from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("login", views.login_view, name="login"),
    path("register", views.register_view, name="register"),
    path("catalogue", views.catalogue, name="catalogue"),
    path('pet/<int:pet_id>/', views.pet, name='pet'),
    path('adoption/<int:pet_id>/', views.request_adoption, name='adoption'),
    path("account", views.account, name="account"),
    path("adoptions", views.adoptions, name="adoptions"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
