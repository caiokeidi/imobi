from django.urls import path
from . import views
 
urlpatterns = [
    path('servicos', views.servicos, name='servicos'),
    path('sobre', views.sobre, name='sobre'),
    path('contato', views.contato, name='contato')
]
