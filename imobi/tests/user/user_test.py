from django.contrib.auth.models import User

def test_user_create(db):
    user_count = User.objects.count() + 1
    User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    assert User.objects.count() == user_count