from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect, HttpResponse
from django.contrib.auth.models import User
from apps.imoveis.models import Imoveis, imagens
from easy_thumbnails.files import get_thumbnailer

def cadastro_imoveis(request):
    
    if request.user.is_authenticated:
        if request.method=='POST':
            
            corretor = get_object_or_404(User, pk=request.user.id)
            cliente = request.POST['cliente']
            cidade = request.POST['cidade']
            bairro = request.POST['bairro']
            rua = request.POST['rua']
            numero = request.POST['numero']
            complemento = request.POST['complemento']
            tipo_negocio = request.POST['tipo_negocio']
            tipo_imovel = request.POST['tipo_imovel']
            valor_aluguel = request.POST['valor_aluguel']
            valor_venda = request.POST['valor_venda']
            valor_iptu = request.POST['valor_iptu']
            valor_condominio = request.POST['valor_condominio']
            area = request.POST['area']
            quartos = request.POST['quartos']
            suites = request.POST['suites']
            banheiros = request.POST['banheiros']
            vagas = request.POST['vagas']
            andar = request.POST['andar']

            metro_proximo = False
            if 'metro_proximo' in request.POST:
                metro_proximo = True

            mobiliado = False
            if 'mobiliado' in request.POST:
                mobiliado = True

            descricao = request.POST['descricao']

            publicado = False
            if 'publicado' in request.POST:
                publicado = True


            imovel=Imoveis.objects.create(corretor=corretor, cliente=cliente, cidade=cidade, bairro=bairro, rua=rua,
            numero=numero, complemento=complemento, tipo_negocio=tipo_negocio, tipo_imovel=tipo_imovel, valor_aluguel=valor_aluguel,
            valor_venda=valor_venda, valor_iptu=valor_iptu, valor_condominio=valor_condominio, area=area, quartos=quartos,
            suites=suites, banheiros=banheiros, vagas=vagas, andar=andar, metro_proximo=metro_proximo, mobiliado=mobiliado,
            descricao=descricao, publicado=publicado)

            imovel.save()
            
            imgs = request.FILES.getlist('imagens')
            for img in imgs:
                imagens.objects.create(foto=img, imoveis=imovel)
            

            return render(request, 'imoveis/cadastro.html')  
        else:
            return render(request, 'imoveis/cadastro.html')   
    else:
        return redirect('login')
