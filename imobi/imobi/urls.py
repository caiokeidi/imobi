
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('apps.imoveis.urls')),
    path('imobiliaria/', include('apps.imobiliaria.urls')),
    path('admin/', admin.site.urls)
]
