"""
URL configuration for main project.
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from main import views as main_views
from authorisation import views as auth_views

urlpatterns = [
    # admin #
    path('admin/', admin.site.urls),

    # USER LINKS
    path('', include('django.contrib.auth.urls')),

    # main #
    path('', main_views.main, name='Main'),
    path('vpn/', main_views.vpn, name='VPN'),
    path('<str:site>/<path:url>', main_views.brows_vpn, name='VPNSite'),
    path('add_site/', main_views.add_site, name='AddSite'),

    # authorisation #
    path('closed/', auth_views.closed_access, name='closed_access'),
    path('profile/', auth_views.profile_view, name='profile'),
    path('singup/', auth_views.singup, name='singup'),
    path('edit_profile/', auth_views.edit_profile, name='edit_profile'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
