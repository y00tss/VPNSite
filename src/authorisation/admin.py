from django.contrib import admin
from authorisation.models import CustomUser


@admin.register(CustomUser)
class ProxyAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')  # noqa
    list_filter = ('username',)
    search_fields = ('username',)
