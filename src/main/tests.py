from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from main.models import WebSites


class PublicTestViews(TestCase):
    """Test views that don't need auth"""

    def test_get_main_page(self):
        """Test getting main page for not auth user"""
        response = self.client.get(reverse('Main'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/main.html')

    def test_create_a_site_without_auth(self):
        """Test creating a site with not auth user"""
        response = self.client.get(reverse('AddSite'))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/closed/?next=/add_site/')

    def test_browse_vpn_without_auth(self):
        """Test browse vpn with not auth user"""
        site_name = 'Test Site'
        site_url = 'http://example.com'

        response = self.client.get(reverse('VPNSite', args=[site_name, site_url]))  # noqa

        self.assertEqual(response.status_code, 302)


class ProtectedTestViews(TestCase):
    """Test views that need auth"""

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.site = WebSites.objects.create(
            site_name='Test Site',
            site_url='http://example.com',
            user=self.user
        )
        self.url = reverse('VPNSite', args=[self.site.site_name, self.site.site_url])  # noqa

    def test_create_a_site_with_auth_user(self):
        """Test creating a site with auth user"""
        self.client.force_login(self.user)
        response = self.client.get(reverse('AddSite'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/add_site.html')

        payload = {
            'site_name': 'NewSite',
            'site_url': 'http://google.com',
        }
        WebSites.objects.create(user=self.user, site_name=payload['site_name'], site_url=payload['site_url'])  # noqa

        new_site = WebSites.objects.get(site_name='NewSite')
        self.assertEqual(new_site.site_name, payload['site_name'])

    def test_create_a_exist_site_with_auth_user(self):
        """Test creating a exist site with auth user"""
        self.client.force_login(self.user)
        WebSites.objects.create(
            site_name='Old',
            site_url='http://exampleold.com',
            user=self.user
        )

        payload = {
            'site_name': 'Old',
            'site_url': 'http://exampleold.com',
            'user': self.user,
        }
        response = self.client.post(reverse('AddSite'), payload)

        self.assertEqual(response.status_code, 200)
        sites = WebSites.objects.filter(site_name='Old')
        self.assertEqual(len(sites), 1)

    def test_vpn_with_auth_user(self):
        """Test browse vpn with auth user"""
        self.client.force_login(self.user)
        site_name = self.site.site_name
        site_url = self.site.site_url

        response = self.client.get(reverse('VPNSite', args=[site_name, site_url]))  # noqa

        self.assertEqual(response.status_code, 200)
