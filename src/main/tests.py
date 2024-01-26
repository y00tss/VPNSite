from django.test import TestCase, Client

from authorisation.models import CustomUser as User


# from .models import WebSites, Proxy
# from main.form import ADDSite
# from main.views import main, add_site, vpn


class ViewsTestCase(TestCase):
    """Test case for views"""

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword',
        )
