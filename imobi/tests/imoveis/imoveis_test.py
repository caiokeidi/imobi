from imoveis.views import imovel, index
from django.contrib.auth.models import User
from django.urls import reverse
import pytest



def teste_200_index(rf, db):
    request = rf.get('')
    object = index(request)
    assert 200 == object.status_code

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