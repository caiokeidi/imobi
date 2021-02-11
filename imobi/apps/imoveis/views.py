from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.db.models import Count
from django.contrib.auth.models import User
from .models import Imoveis, imagens
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json

def index(request):
    
    imoveis = Imoveis.objects.all().order_by("id") ##Precisei colocar parar parar o erro do pytest
    cidade_bairro_JSON = json.dumps(cidade_bairro())

    paginator = Paginator(imoveis, 3)
    page = request.GET.get('page')
    imoveis_por_pagina = paginator.get_page(page)

    dados={
        'imoveis': imoveis_por_pagina,
        'cidade_bairro': cidade_bairro_JSON
    }

    return render(request, 'imoveis/index.html', dados)

def imovel(request, imovel_id):
    imovel = get_object_or_404(Imoveis, pk=imovel_id)

    imovel_a_exibir = {
        'imovel': imovel
    }

    return render(request, 'imoveis/imovel.html', imovel_a_exibir)
   
def busca(request):
    dados = {}

    if request.method == 'POST':
        tipo_negocio = request.POST['tipo_negocio']
        cidade = request.POST['cidade']
        bairro = request.POST['bairro']
        tipo_imovel = request.POST['tipo_imovel']
        valor_min = request.POST['valor_min']
        valor_max = request.POST['valor_max']

        if valor_min == '':
            valor_min = 0
        if valor_max == '':
            valor_max = 10000000

        if tipo_negocio == 'Aluguel':
            imoveis_buscados = Imoveis.objects.filter(tipo_negocio=tipo_negocio, cidade=cidade,
                                bairro = bairro, tipo_imovel=tipo_imovel, valor_aluguel__lte = valor_max, valor_aluguel__gte = valor_min)
        else:
            imoveis_buscados = Imoveis.objects.filter(tipo_negocio=tipo_negocio, cidade=cidade,
                                bairro = bairro, tipo_imovel=tipo_imovel, valor_venda__lte = valor_max, valor_venda__gte = valor_min)

        cidade_bairro_JSON = json.dumps(cidade_bairro())

        dados={
            'imoveis': imoveis_buscados,
            'cidade_bairro': cidade_bairro_JSON
        }


    return render(request, 'imoveis/busca.html', dados)

def cadastro_imoveis(request):
    if request.user.is_authenticated:
        return render(request, 'imoveis/cadastro.html')   
    else:
        return redirect('login')

def cidade_bairro():
    dict_cb_query = Imoveis.objects.values('bairro', 'cidade', 'tipo_negocio', 'tipo_imovel').annotate(dcount=Count('bairro'))
    array_cb = []
    for cb in dict_cb_query:
        array_cb.append(cb)
    
    return array_cb

