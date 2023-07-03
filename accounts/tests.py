from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

class AccountManagerTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email="test@test.com", password="test")
        self.assertEqual(user.email, "test@test.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

        try:
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email="")
        with self.assertRaises(ValueError):
            User.objects.create_user(email="", password="test")

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(email="test@test.com", password="test")
        self.assertEqual(admin_user.email, "test@test.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

        try:
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser("test@test.com", password="test", is_superuser=False)

class RegistrationTests(TestCase):
    def setUp(self) -> None:
        self.email = 'test@test.com'
        self.password1 = 'GreatestTest'
        self.password2 = 'GreatestTest'

    def test_register_url(self):
        response = self.client.get("/accounts/register/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name="registration/register.html")

    def test_register_view_name(self):
        response = self.client.get(reverse('accounts:register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='registration/register.html')

    def test_user_creation_form(self):
        response = self.client.post(reverse('accounts:register'), data={
            'email': self.email,
            'password1': self.password1,
            'password2': self.password2,
        })
        # Checking for redirect to index after user registration
        self.assertEqual(response.status_code, 302)
        users = get_user_model().objects.all()
        self.assertEqual(users.count(), 1)

        
    