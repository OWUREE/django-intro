from django.urls import path, include
from django.contrib import admin
from polls import views,viewsets 
from rest_framework import routers

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'data', viewsets.DustBinViewSet)


urlpatterns = [
    path('', views.index, name="index"),
    path('logout/', views.logout, name="LOGOUT"),
    path('register/', views.register, name="register"),
    path('login.html/', views.login, name="LOGIN"),
    path('layout/', views.layout, name="layout"),
    path('about.html/', views.about, name="ABOUT" ),
    path('api/', include(router.urls)),
]
