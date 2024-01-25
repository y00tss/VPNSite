from main.models import WebSites, Proxy
from django import forms


# -------------------------------------------Adding site to user profile-----------------------------------------------
class ADDSite(forms.ModelForm):
    class Meta:
        model = WebSites
        fields = ('site_name', 'site_url')


# -------------------------------------------Adding site to user profile-----------------------------------------------

# --------------------------------------------------Adding proxy-------------------------------------------------------
'''All forms below are not used in the project'''


# this form is used to add proxy to the database by moderator or admin(in the future)now it can be done only by admin dj
class ProxyForm(forms.Form):
    class Meta:
        model = Proxy
        fields = ('proxy_ip', 'proxy_port', 'proxy_login', 'proxy_password')


class WebSitesForm(forms.Form):
    class Meta:
        model = WebSites
        fields = ('site_name', 'site_url')
