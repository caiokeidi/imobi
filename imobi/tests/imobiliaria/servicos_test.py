from imobiliaria.views import servicos

def teste_200_imobiliaria_servicos(rf, db):
    request = rf.get('/imobiliaria/servicos')
    object = servicos(request)
    assert 200 == object.status_code
