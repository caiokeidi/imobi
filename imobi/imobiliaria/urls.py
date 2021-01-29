from django.urls import path
from . import views
 
urlpatterns = [
    path('servicos', views.servicos, name='servicos')
]
