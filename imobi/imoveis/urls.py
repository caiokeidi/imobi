from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.index, name='index'),
    path('imovel/<int:imovel_id>', views.imovel, name='imovel'),
    path('imovel/busca', views.busca, name='busca')
]
