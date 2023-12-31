from django.conf import settings
from django.db import models


# Create your models here.
# --------------------------------------------------Table of Proxy------------------------------------------------------
class Proxy(models.Model):
    ip = models.GenericIPAddressField(verbose_name='IP')
    port = models.IntegerField(verbose_name='Port')
    username = models.CharField(verbose_name='Username', max_length=50)
    password = models.CharField(verbose_name='Password', max_length=50)
    available = models.BooleanField(verbose_name='Available', default=True)

    def __str__(self):
        return f'{self.ip}:{self.port}'

    def order_proxy(self):
        self.available = False
        self.save()

    class Meta:
        verbose_name = 'Proxy'
        verbose_name_plural = 'Proxies'


# --------------------------------------------------Table of Proxy------------------------------------------------------

# -------------------------------------------------Table of WebSites----------------------------------------------------
class WebSites(models.Model):
    site_name = models.CharField(verbose_name='Site name', max_length=50)
    site_url = models.URLField(verbose_name='Site url')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='User')

    def __str__(self):
        return self.site_name

    class Meta:
        verbose_name = 'Site'
        verbose_name_plural = 'Sites'


# -------------------------------------------------Table of WebSites----------------------------------------------------

# ----------------------------------------------Table of user activity-------------------------------------------------
class SiteAttended(models.Model):
    site = models.ForeignKey(WebSites, on_delete=models.CASCADE, verbose_name='Site')
    proxy = models.ForeignKey(Proxy, on_delete=models.CASCADE, verbose_name='Proxy')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='User')
    date = models.DateTimeField(verbose_name='Date', auto_now_add=True)

    def __str__(self):
        return f'{self.site} - {self.proxy}'

    class Meta:
        verbose_name = 'Site attended'
        verbose_name_plural = 'Sites attended'

# ----------------------------------------------Table of user activity-------------------------------------------------
