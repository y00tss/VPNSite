from django.test import TestCase, Client
from django.urls import reverse
from authorisation.models import CustomUser


class ViewsTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user(username='testuser', email='test@example.com',
                                                   password='testpassword')

    def test_closed_access(self):
        response = self.client.get(reverse('closed_access'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/constant_templates/closed.html')
        self.assertEqual(response.context['title'], 'closed_access')

    def test_profile_view_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authorisation/profile.html')
        # Add more assertions if needed based on context or data displayed on the profile page

    def test_edit_profile_GET(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('edit_profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authorisation/editprofile.html')
