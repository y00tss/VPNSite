from django.contrib import admin
from main.models import Proxy, WebSites, Statistic


@admin.register(Proxy)
class ProxyAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'ip', 'port', 'available')  # noqa
    list_filter = ('available', 'ip')
    search_fields = ('ip', 'available', 'username')


@admin.register(WebSites)
class WebSiteAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'site_url', 'user')  # noqa
    list_filter = ('user', 'site_name')
    search_fields = ('user', 'site_name')


@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
    list_display = ('user', 'url', 'counter')
    list_filter = ('counter', 'user')
    search_fields = ('user', 'url', 'counter')
