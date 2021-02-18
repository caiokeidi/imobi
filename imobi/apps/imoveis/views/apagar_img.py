
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect, HttpResponse
from django.contrib.auth.models import User
from apps.imoveis.models import imagens


def apagar_img(request, img_id):
    if request.user.is_authenticated:
        img = imagens.objects.filter(id=img_id)

        img.delete()

        return HttpResponse(request, 'Success')
    
    return HttpResponse(request, 'Fail')
