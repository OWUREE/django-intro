from django.urls import path
from polls import views
# Create your urls here.


urlpatterns = [
    path('', views.index),

    path('home', views.register)
]
