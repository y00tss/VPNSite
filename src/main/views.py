import requests
from django.contrib.auth.decorators import login_required
from django.shortcuts import (
    render,
    redirect,
)
from main.models import (
    Proxy,
    WebSites,
    Statistic,
)
from main.form import ADDSite

from bs4 import BeautifulSoup
from urllib.parse import (
    urljoin,
    urlparse,
)


def main(request):
    """View for main page"""
    return render(
        request,
        'main/main.html',
        {
            'title': 'Main',
            'name': 'VPNSheepFish',
        },
    )


@login_required
def add_site(request):
    """View for add site page"""
    if request.method == 'POST':
        form = ADDSite(request.POST)
        if form.is_valid():
            website = form.save(commit=False)
            website.user = request.user
            website.save()
            return redirect('VPN')
    else:
        form = ADDSite()
    return render(
        request,
        'main/add_site.html',
        {
            'form': form,
            'title': 'SheepFish',
        },
    )


@login_required
def vpn(request):
    """View for choose site and proxy page"""
    if request.method == 'POST':
        website_id = request.POST.get('website')

        name_of_website = WebSites.objects.get(pk=website_id)

        return redirect('VPNSite', site=name_of_website.site_name, url=name_of_website.site_url)  # noqa

    websites = WebSites.objects.filter(user=request.user)
    proxy = Proxy.objects.filter(available=True)
    return render(
        request,
        'main/vpn.html',
        {
            'title': 'SheepFish',
            'proxy': proxy,
            'websites': websites,
        },
    )


@login_required
def brows_vpn(request, site, url):
    """View for browsing site with VPN"""
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, 'html.parser')
    for code_site in soup.find_all('a', href=True):
        href = code_site['href']
        target_url = urljoin(url, href)

        if urlparse(target_url).netloc == urlparse(url).netloc:
            code_site['href'] = f'http://127.0.0.1:8000/{site}/{target_url}'

    content_type = response.headers['content-type']
    content = str(soup)
    data_sent = len(request.body)
    data_received = len(response.content)

    parsed_url = urlparse(url).scheme + '://' + urlparse(url).netloc
    visited_url, created = Statistic.objects.get_or_create(
        user=request.user,
        url=parsed_url,
    )

    visited_url.data_sent += data_sent
    visited_url.data_received += data_received

    if urlparse(url).path == '/' or urlparse(url).path == '':
        visited_url.counter += 1
    visited_url.save()

    return render(
        request,
        'main/vpn_view.html',
        {
            'title': f'VPN: {site}',
            'content': content,
            'content_type': content_type,
            'url': url,
        }
    )
