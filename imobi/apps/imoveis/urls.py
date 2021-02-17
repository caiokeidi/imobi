from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.index, name='index'),
    path('imovel/<int:imovel_id>', views.imovel, name='imovel'),
    path('imovel/busca', views.busca, name='busca'),
    path('imovel/cadastro', views.cadastro_imoveis, name='cadastro_imoveis'),
    path('imovel/editar/<int:imovel_id>', views.editar_imovel, name='editar_imovel'),
    path('imovel/apagar/img/<int:img_id>', views.apagar_img, name='apagar_img')
]
