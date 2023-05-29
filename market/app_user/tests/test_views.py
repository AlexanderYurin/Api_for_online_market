# from time import sleep
# import tempfile
#
# from django.conf import settings
# from django.contrib.auth.models import User
#
# from django.test import TestCase
# from django.shortcuts import reverse
#
# from app_shop.models import Shop, Good
# from app_user.models import Profile, Order
#
#
# class TestViewRegistrationUser(TestCase):
#     def test_view_url_exists_at_desired_location(self):
#         resp = self.client.get('/user/registration/')
#         self.assertEqual(resp.status_code, 200)
#
#     def test_view_url_accessible_by_name(self):
#         resp = self.client.get(reverse('registration'))
#         self.assertEqual(resp.status_code, 200)
#
#     def test_view_uses_correct_template(self):
#         resp = self.client.get(reverse('registration'))
#         self.assertEqual(resp.status_code, 200)
#         self.assertTemplateUsed(resp, 'app_user/registration.html')
#
#
# class TestViewLoginUser(TestCase):
#
#     @classmethod
#     def setUpTestData(cls):
#         test_user1 = User.objects.create_user(username='testuser1', password='12345',
#                                               first_name='first_name', last_name='last_name',
#                                               email='email@mail.ru')
#
#     def test_view_url_exists_at_desired_location(self):
#         resp = self.client.get('/user/login/')
#         self.assertEqual(resp.status_code, 200)
#
#     def test_view_url_accessible_by_name(self):
#         resp = self.client.get(reverse('login'))
#         self.assertEqual(resp.status_code, 200)
#
#     #
#     def test_view_uses_correct_template(self):
#         resp = self.client.get(reverse('login'))
#         self.assertEqual(resp.status_code, 200)
#         self.assertTemplateUsed(resp, 'app_user/login.html')
#
#     def test_login_user(self):
#         login = self.client.login(username='testuser1', password='12345')
#         resp = self.client.get(reverse('main'))
#         self.assertEqual(str(resp.context['user']), 'testuser1')
#         self.assertEqual(resp.status_code, 200)
#
#
# TEMP_MEDIA_ROOT = tempfile.mkdtemp(dir=settings.BASE_DIR)
#
#
# class TestViewProfileInfoCache(TestCase):
#
#     def setUp(self):
#         test_user1 = User.objects.create_user(
#             username='testuser1', password='12345',
#             first_name='first_name', last_name='last_name',
#         )
#
#         self.test_user1_profile = Profile.objects.create(
#             user=test_user1, first_name=test_user1.first_name,
#             last_name=test_user1.last_name
#         )
#
#         self.test_shop1 = Shop.objects.create(title='TestShop1', description='TestDescription1', sale=10)
#         self.test_good1 = Good.objects.create(shop=self.test_shop1, title='TestGood1', price=100)
#         self.test_order_user1 = Order.objects.create(profile=self.test_user1_profile, good=self.test_good1)
#
#     def test_cache_promo_and_offers(self):
#         login = self.client.login(username='testuser1', password='12345')
#         resp = self.client.get(reverse('profile'))
#         self.assertTrue(self.test_shop1 in resp.context['caches_promo_and_offers']['promo'])
#         self.assertTrue(self.test_good1 in resp.context['caches_promo_and_offers']['offers'])
#         test_shop2 = Shop.objects.create(title='TestShop2', description='TestDescription2', sale=10)
#         test_good2 = Good.objects.create(shop=test_shop2, title='TestGood2', price=100)
#         resp = self.client.get(reverse('profile'))
#         self.assertFalse(test_shop2 in resp.context['caches_promo_and_offers']['promo'])
#         self.assertFalse(test_good2 in resp.context['caches_promo_and_offers']['offers'])
#         sleep(11)
#         resp = self.client.get(reverse('profile'))
#         self.assertTrue(test_shop2 in resp.context['caches_promo_and_offers']['promo'])
#         self.assertTrue(test_good2 in resp.context['caches_promo_and_offers']['offers'])
#
#     def test_cache_order_history(self):
#         login = self.client.login(username='testuser1', password='12345')
#         resp = self.client.get(reverse('profile'))
#         self.assertEqual(resp.context['order'].count(), 1)
#         test_order_user1 = Order.objects.create(profile=self.test_user1_profile, good=self.test_good1)
#         resp = self.client.get(reverse('profile'))
#         print(resp.context)
#         self.assertEqual(resp.context['order'].count(), 1)
#         resp = self.client.get(reverse('profile'))
#         self.assertEqual(resp.context['order'].count(), 2)
#
#
# class TestRegisterUser(TestCase):
#     def test_registration_user(self):
#         form_data = {
#             'username': 'testuser1',
#             'password1': 'Cfif12345',
#             'password2': 'Cfif12345',
#             'first_name': 'first_name',
#             'last_name': 'last_name',
#         }
#         resp = self.client.post(
#             reverse('registration'),
#             data=form_data
#         )
#         self.assertRedirects(resp, reverse('main'))
#         self.assertEqual(User.objects.get(id=1).username, 'testuser1')
#         self.assertEqual(User.objects.get(id=1).first_name, 'first_name')
#         self.assertEqual(User.objects.get(id=1).last_name, 'last_name')
