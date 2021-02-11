from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

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
                return redirect('index')

            else:
                print('Senha ou Usuário Incorreto')
                return redirect('login')

        else:
            print('Usuário não existe')

    return render(request, 'corretor/login.html')


def logout(request):
    auth.logout(request)
    return redirect('index')

