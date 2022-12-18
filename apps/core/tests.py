from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

class LoginViewTestCase(TestCase):
  def setUp(self):
    User.objects.create_user(
      username='testuser',
      password='testpass'
    )

  def test_login_success(self):
    response = self.client.post(reverse('login_page'), {
      'username': 'testuser',
      'password1': 'testpass'
    })
    self.assertEqual(response.status_code, 200)

  def test_login_failure(self):
    response = self.client.post(reverse('login_page'), {
      'username': 'testuser',
      'password1': 'incorrect'
    })
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, '', html=True)


class RegistrationViewTestCase(TestCase):
  def test_registration_success(self):
    response = self.client.post(reverse('register_page'), {
      'username': 'testuser',
      'first_name': 'testfirst',
      'last_name': 'testlast',
      'password1': 'testpass',
      'password2': 'testpass',
      'email': 'test@example.com'
    })
    self.assertEqual(response.status_code, 302)
    self.assertTrue(User.objects.filter(username='testuser').exists())

  def test_registration_failure(self):
    response = self.client.post(reverse('register_page'), {
      'username': 'testuser',
      'first_name': 'testfirst',
      'last_name': 'testlast',
      'password1': 'testpass',
      'password2': 'incorrect',
      'email': 'test@example.com'
    })
    self.assertEqual(response.status_code, 302)