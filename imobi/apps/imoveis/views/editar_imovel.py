from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect, HttpResponse
from django.contrib.auth.models import User
from apps.imoveis.models import Imoveis, imagens
from easy_thumbnails.files import get_thumbnailer
from django.conf import settings


def editar_imovel(request, imovel_id):

    if request.method=='POST':
        i = get_object_or_404(Imoveis, pk=imovel_id)

        v_aluguel = request.POST['valor_aluguel']
        v_venda = request.POST['valor_venda']
        v_iptu = request.POST['valor_iptu']
        v_condominio = request.POST['valor_condominio']

        i.corretor = get_object_or_404(User, pk=request.user.id)
        i.cliente = request.POST['cliente']
        i.cidade = request.POST['cidade']
        i.bairro = request.POST['bairro']
        i.rua = request.POST['rua']
        i.numero = request.POST['numero']
        i.complemento = request.POST['complemento']
        i.tipo_negocio = request.POST['tipo_negocio']
        i.tipo_imovel = request.POST['tipo_imovel']
        i.valor_aluguel = float(v_aluguel.replace(',', '.'))
        i.valor_venda = float(v_venda.replace(',', '.'))
        i.valor_iptu = float(v_iptu.replace(',', '.'))
        i.valor_condominio = float(v_condominio.replace(',', '.'))
        i.area = request.POST['area']
        i.quartos = request.POST['quartos']
        i.suites = request.POST['suites']
        i.banheiros = request.POST['banheiros']
        i.vagas = request.POST['vagas']
        i.andar = request.POST['andar']

        i.metro_proximo = False
        if 'metro_proximo' in request.POST:
            i.metro_proximo = True

        i.mobiliado = False
        if 'mobiliado' in request.POST:
            i.mobiliado = True

        descricao = request.POST['descricao']

        i.publicado = False
        if 'publicado' in request.POST:
            i.publicado = True


        i.save()
        
        imgs = request.FILES.getlist('imagens')
        for img in imgs:
            imagens.objects.create(foto=img, imoveis=i)
        

        return redirect('imoveis_corretor')

    else:
        imovel = get_object_or_404(Imoveis, pk=imovel_id)
        imgs = imagens.objects.filter(imoveis=imovel_id)
        imgs_and_thumbs = []
        for i in imgs:
            element = retorna_img_thumbnail(i)

            imgs_and_thumbs.append(element)

        
        imovel_a_exibir = {
            'imovel': imovel,
            'imagens': imgs_and_thumbs
        }

        return render(request, 'imoveis/editar_imovel.html', imovel_a_exibir)


def retorna_img_thumbnail(i):
    ###Precisei colocar o replace(media) pois por algum motivo ele estava dando media duplicado no url
    element = {}
    thumbnail = get_thumbnailer(settings.MEDIA_ROOT.replace('\media', '')+i.foto.url)['miniatura']
    element['thumb'] = thumbnail
    element['img'] = i

    return element