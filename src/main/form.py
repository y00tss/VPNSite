from main.models import WebSites, Proxy
from django import forms


class ADDSite(forms.ModelForm):
    """Form for adding site to user profile"""

    class Meta:
        model = WebSites
        fields = (
            'site_name',
            'site_url',
        )


# this form is used to add proxy to the database by moderator or admin(in the future)now it can be done only by admin dj  # noqa
class ProxyForm(forms.Form):
    """Form for adding proxy to the database"""

    class Meta:
        model = Proxy
        fields = (
            'proxy_ip',
            'proxy_port',
            'proxy_login',
            'proxy_password',
        )


class WebSitesForm(forms.Form):
    """Form for adding site to the database"""

    class Meta:
        model = WebSites
        fields = (
            'site_name',
            'site_url',
        )
