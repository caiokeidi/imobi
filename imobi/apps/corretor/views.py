from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from apps.imoveis.models import Imoveis, imagens

def login(request):
    
    if request.method == 'POST':
        usuario = request.POST['usuario']
        senha = request.POST['senha']

        userFilter = User.objects.filter(username=usuario).exists()

        if userFilter:
            try:
                user = auth.authenticate(request, username = usuario, password = senha)
                
            except:
                user = None
            
            if user is not None:
                auth.login(request, user)
                print(f'Usuário {user} logado')
                return redirect('dashboard')

            else:
                print('Senha ou Usuário Incorreto')
                return redirect('login')

        else:
            print('Usuário não existe')

    return render(request, 'corretor/login.html')


def logout(request):
    auth.logout(request)
    return redirect('index')

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'corretor/dashboard.html')
    else:
        return redirect('login')
    


def imoveis_corretor(request):
    imoveis_objects = Imoveis.objects.all().order_by("id").filter(corretor=request.user.id)
    imoveis = []
    
    for obj in imoveis_objects:
        imovel = {}
        img = imagens.objects.filter(imoveis=obj).first()
        
        imovel['imovel'] = obj
        imovel['img'] = img

        imoveis.append(imovel)

    dados={
        'imoveis': imoveis
    }

    return render(request, 'corretor/imoveis_corretor.html', dados)