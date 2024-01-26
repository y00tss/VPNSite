"""
Tests for user model
"""
from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from authorisation.models import CustomUser


class TestPublicUser(TestCase):
    """Tests user without authentication"""

    def setUp(self):
        self.client = Client()

    def test_get_redirect_page(self):
        """Test user page view for non auth users for getting Closed Access"""
        url = reverse('profile')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 302)

    def test_user_page_without_auth(self):
        """Test user page without auth and redirect"""
        url = reverse('profile')
        response = self.client.get(url, follow=True)

        self.assertEqual(response.status_code, 200)

    def test_user_registration(self):
        """Test creating new user"""
        url = reverse('singup')
        form_data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'newpassword123S!',
            'password2': 'newpassword123S!'
        }

        response = self.client.post(url, form_data, follow=True)

        self.assertEqual(response.status_code, 200)

        self.assertTrue(
            get_user_model().objects.filter(username='newuser'
                                            ).exists())


class TestPrivateUser(TestCase):
    """Test users with authentication"""

    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123',
        )

        self.client = Client()
        self.client.login(username='testuser', password='testpass123')

    def test_get_user_page_access_for_authenticated_users(self):
        """Test user page view for authenticated users"""
        response = self.client.get(reverse('profile'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authorisation/profile.html')
        self.assertEqual(response.context['user'], self.user)

    def test_signup_view(self):
        """Test SignUp view and Check creation users """
        response = self.client.get(reverse('singup'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/registration.html')

        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertTrue(self.user.check_password('testpass123'))

    def test_creating_exists_user(self):
        """Test creating user that already exists by USERNAME or EMAIL"""
        url = reverse('singup')
        form_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'testpass123',
        }

        response = self.client.post(url, form_data, follow=True)

        self.assertEqual(response.status_code, 200)

        self.assertEqual(
            get_user_model().objects.filter(username='testuser'
                                            ).count(), 1)

    def test_edit_profile_view_accessible(self):
        """Test if the edit profile view is accessible"""
        url = reverse('edit_profile')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authorisation/editprofile.html')

    def test_edit_profile_form_submission(self):
        pass
