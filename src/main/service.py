"""
Fill up proxy database for testing
"""
from main.models import Proxy


def format_size(size_in_bytes):
    # Function to format the size in a human-readable format
    for unit in ['B', 'KB', 'MB']:
        if size_in_bytes < 1024.0:
            return f"{size_in_bytes:.2f} {unit}"
        size_in_bytes /= 1024.0


def create_proxy():
    """Create a proxy object for the current request."""
    if Proxy.objects.filter(ip='188.74.210.21').exists():
        pass
    else:
        proxy = Proxy.objects.create(
            ip='188.74.210.21',
            port='6100',
            username='hwongjea',
            password='wfxvb0auosak',
        )
        proxy.save()
