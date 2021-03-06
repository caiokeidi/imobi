from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect, HttpResponse
from django.db.models import Count
from django.contrib.auth.models import User
from apps.imoveis.models import Imoveis, imagens
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json
from easy_thumbnails.files import get_thumbnailer
from django.conf import settings



def index(request):
    imoveis_objects = Imoveis.objects.all().order_by("id") ##Precisei colocar parar parar o erro do pytest
    imoveis = []
    for obj in imoveis_objects:
        imovel = {}
        img = imagens.objects.filter(imoveis=obj).first()
        
        imovel['imovel'] = obj
        imovel['img'] = img

        imoveis.append(imovel)
    
    cidade_bairro_JSON = json.dumps(cidade_bairro())

    paginator = Paginator(imoveis, 6)
    page = request.GET.get('page')
    imoveis_por_pagina = paginator.get_page(page)

    dados={
        'imoveis': imoveis_por_pagina,
        'cidade_bairro': cidade_bairro_JSON
    }


    return render(request, 'imoveis/index.html', dados)


def imovel(request, imovel_id):
    imovel = get_object_or_404(Imoveis, pk=imovel_id)
    imgs = imagens.objects.filter(imoveis=imovel_id)
    imgs_and_thumbs = []
    for i in imgs:
        ###Precisei colocar o replace(media) pois por algum motivo ele estava dando media duplicado no url
        element = {}
        thumbnail = get_thumbnailer(settings.MEDIA_ROOT.replace('\media', '')+i.foto.url)['miniatura']
        element['thumb'] = thumbnail
        element['img'] = i

        imgs_and_thumbs.append(element)
    
    print(imgs_and_thumbs)


    imovel_a_exibir = {
        'imovel': imovel,
        'imagens': imgs_and_thumbs
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
            
    print(dados)
    return render(request, 'imoveis/busca.html', dados)



def cidade_bairro():
    dict_cb_query = Imoveis.objects.values('bairro', 'cidade', 'tipo_negocio', 'tipo_imovel').annotate(dcount=Count('bairro'))
    array_cb = []
    for cb in dict_cb_query:
        array_cb.append(cb)
    
    return array_cb

def retorna_imoveis_buscados(request):
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

    return dados


def retorna_img_thumbnail(i):
    ###Precisei colocar o replace(media) pois por algum motivo ele estava dando media duplicado no url
    element = {}
    thumbnail = get_thumbnailer(settings.MEDIA_ROOT.replace('\media', '')+i.foto.url)['miniatura']
    element['thumb'] = thumbnail
    element['img'] = i

    return element

