from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Imoveis, imagens

def index(request):

    imoveis = Imoveis.objects.all()

    dados={
        'imoveis': imoveis
    }
    

    return render(request, 'imoveis/index.html', dados)

def imovel(request, imovel_id):
    imovel = get_object_or_404(Imoveis, pk=imovel_id)

    imovel_a_exibir = {
        'imovel': imovel
    }

    return render(request, 'imoveis/imovel.html', imovel_a_exibir)

