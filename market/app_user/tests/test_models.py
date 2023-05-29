from django.contrib.auth.models import User
from django.test import TestCase

from app_user.models import Profile


class TestModels(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user1 = User.objects.create_user(username='testuser1', password='12345',
                                              first_name='first_name', last_name='last_name',
                                              email='email@mail.ru')

        test_user1_profile = Profile.objects.create(
            user=test_user1, first_name=test_user1.first_name,
            last_name=test_user1.last_name, email=test_user1.email
        )

    def test_models_user_OneToOneField(self):
        user = Profile.objects.get(id=1).user.username
        self.assertEqual(user, 'testuser1')


