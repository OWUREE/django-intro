from django.urls import path
from polls import views
# Create your urls here.


urlpatterns = [
    path('', views.index, name="index"),
    path('register', views.register, name="register"),
    path('question/<int:id>', views.question, name="question"),
    path('layout', views.layout, name="layout"),
    path('about', views.about, name="about" )
]
