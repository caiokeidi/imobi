from apps.imoveis.views import imovel, index
from django.contrib.auth.models import User
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.urls import reverse
from django.http import Http404
import pytest



def teste_index_mostra_casas_destaque(rf, db):
    request = rf.get('')
    object = index(request)

    verification = b'Vila Costa'
    assert verification in object.content


def teste_200_imovel_1(rf, db):
    url = reverse(
    'imovel', kwargs={'imovel_id': 1}
    )
    object = imovel(url, imovel_id=1)

    assert 200 == object.status_code


def teste_404_imovel(rf, db):

    with pytest.raises(Http404):
        url = reverse(
        'imovel', kwargs={'imovel_id': 2}
        )
        object = imovel(url, imovel_id=2
        )

def teste_verifica_se_traz_imovel_correto(db):
    url = reverse(
    'imovel', kwargs={'imovel_id': 1}
    )
    object = imovel(url, imovel_id=1)
    verification = b'Mogi das Cruzes'

    assert verification in object.content

