from apps.imoveis.views import index

def teste_200_index(rf, db):
    request = rf.get('')
    object = index(request)
    assert 200 == object.status_code



