from django.shortcuts import render

def servicos(request):
    return render(request, 'imobiliaria/servicos.html')

def sobre(request):
    return render(request, 'imobiliaria/sobre.html')

def contato(request):
    return render(request, 'imobiliaria/contato.html')