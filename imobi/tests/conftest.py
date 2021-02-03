from imobi import settings
from django.contrib.auth.models import User
from django.urls import reverse
import pytest


@pytest.fixture(scope='session')
def django_db_setup():
    settings.DATABASES['default'] = {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': 'localhost',
        'NAME': 'imobi',
    }
