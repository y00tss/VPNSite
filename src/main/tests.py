from django.test import TestCase
from django.test import TestCase, Client
from django.urls import reverse
from authorisation.models import CustomUser as User
from .models import WebSites, Proxy
from main.form import ADDSite
from main.views import main, add_site, vpn


class ViewsTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')

# EMPTY YET
