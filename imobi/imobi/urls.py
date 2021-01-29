
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('imoveis.urls')),
    path('imobiliaria/', include('imobiliaria.urls')),
    path('admin/', admin.site.urls)
]
