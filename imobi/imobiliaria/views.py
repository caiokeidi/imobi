from django.shortcuts import render

def servicos(request):
    return render(request, 'imobiliaria/servicos.html')