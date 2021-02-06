from apps.imobiliaria.views import sobre

def teste_200_imobiliaria_sobre(rf, db):
    request = rf.get('/imobiliaria/sobre')
    object = sobre(request)
    assert 200 == object.status_code
