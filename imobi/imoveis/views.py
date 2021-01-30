from django.shortcuts import render
from .models import Imoveis, imagens

def index(request):

    imoveis = Imoveis.objects.all()

    dados={
        'imoveis': imoveis
    }
    

    return render(request, 'imoveis/index.html', dados)


