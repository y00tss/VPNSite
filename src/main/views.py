import requests
from django.contrib.auth.decorators import login_required
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)
from main.models import (
    Proxy,
    WebSites,
    SiteAttended,
)
from main.form import ADDSite

from main.service import format_size

from VPN.proxy import (
    get_proxy_http,
    get_proxy_data,
)


def main(request):
    """View for main page"""
    return render(
        request,
        'main/main.html',
        {
            'title': 'Main',
            'name': 'VPNSheepF',
        },
    )


@login_required
def add_site(request):
    """View for add site page"""
    if request.user.is_authenticated:
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
                'title': 'Add site',
            },
        )

    else:
        return render(
            request,
            'main/constant_templates/closed.html',
            {'title': 'closed_access'},
        )


def vpn(request):
    """View for choose site and proxy page"""
    if request.user.is_authenticated:
        if request.method == 'POST':
            website_id = request.POST.get('website')
            proxy_id = request.POST.get('proxy')

            name_of_website = WebSites.objects.get(pk=website_id)

            # save statistics
            website = WebSites.objects.get(pk=website_id)
            proxy = Proxy.objects.get(pk=proxy_id)
            SiteAttended.objects.create(site=website, proxy=proxy, user=request.user)  # noqa

            # save data
            request.session['user_proxy'] = proxy_id

            # Redirect to new site_name
            return redirect('VPNSite', site=name_of_website.site_name)

        websites = WebSites.objects.filter(user=request.user)
        proxy = Proxy.objects.filter(available=True)
        return render(
            request,
            'main/vpn.html',
            {
                'title': 'VPN',
                'proxy': proxy,
                'websites': websites,
            },
        )
    else:
        return render(
            request,
            'main/constant_templates/closed.html',
            {'title': 'closed_access'},
        )


@login_required
def brows_vpn(request, site):
    """View for brows site with VPN"""
    if request.user.is_authenticated:
        user_proxy = request.session.get('user_proxy')
        http = get_proxy_http(user_proxy)
        proxy_data = get_proxy_data(user_proxy)

        # get web site chosen by client
        website = get_object_or_404(WebSites, site_name=site, user=request.user)  # noqa
        link_target = website.site_url

        res = requests.get(link_target, proxies=http, verify=False)

        request_size = format_size(len(request.body))
        response_size = len(requests.get(link_target).content)

        return render(
            request,
            'main/vpn_view.html',
            {
                'title': 'VPN',
                'link': res.url,
                'proxy': proxy_data,
                'request_size': request_size,
                'response_size': response_size},
        )
    else:
        return render(
            request,
            'main/constant_templates/closed.html',
            {'title': 'closed_access'},
        )
