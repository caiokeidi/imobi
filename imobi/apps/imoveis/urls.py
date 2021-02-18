from django.urls import path
from .views import *
 
urlpatterns = [
    path('', index, name='index'),
    path('imovel/<int:imovel_id>', imovel, name='imovel'),
    path('imovel/busca', busca, name='busca'),
    path('imovel/cadastro', cadastro_imoveis, name='cadastro_imoveis'),
    path('imovel/editar/<int:imovel_id>', editar_imovel, name='editar_imovel'),
    path('imovel/apagar/img/<int:img_id>', apagar_img, name='apagar_img')
]
