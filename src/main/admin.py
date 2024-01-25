from django.contrib import admin
from main.models import Proxy, WebSites, SiteAttended

# Register your models here.

admin.site.register(Proxy)
admin.site.register(WebSites)
admin.site.register(SiteAttended)
