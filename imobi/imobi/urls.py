
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('apps.imoveis.urls')),
    path('imobiliaria/', include('apps.imobiliaria.urls')),
    path('corretor/', include('apps.corretor.urls')),
    path('admin/', admin.site.urls)
]
