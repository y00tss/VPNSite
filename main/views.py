import requests
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from main.models import Proxy, WebSites, SiteAttended
from main.form import ADDSite
from VPN.proxy import get_proxy_http, get_proxy_data


# -------------------------------------------------Main page-------------------------------------------------------
def main(request):
    return render(request, 'main/main.html', {'title': 'Main',
                                              'name': 'VPNSheepF'})


# -------------------------------------------------Main page-------------------------------------------------------

# -----------------------------------------------Add site page-----------------------------------------------------

# here user can add sites to his personal list
def add_site(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ADDSite(request.POST)
            if form.is_valid():
                website = form.save(commit=False)
                website.user = request.user
                website.save()
                return redirect('AddSite')
        else:
            form = ADDSite()
        return render(request, 'main/add_site.html', {'form': form, 'title': 'Add site'})
    else:
        return render(request, 'main/constant_templates/closed.html', {'title': 'closed_access'})


# -----------------------------------------------Add site page-----------------------------------------------------

# ------------------------------------------------Choose page------------------------------------------------------

# this page is used to choose site from user's list and proxy from the list of available proxies

def vpn(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            website_id = request.POST.get('website')
            proxy_id = request.POST.get('proxy')

            name_of_website = WebSites.objects.get(pk=website_id)

            # save statistics
            website = WebSites.objects.get(pk=website_id)
            proxy = Proxy.objects.get(pk=proxy_id)
            SiteAttended.objects.create(site=website, proxy=proxy, user=request.user)

            # save data
            request.session['user_proxy'] = proxy_id

            # Redirect to new site_name
            return redirect('VPNSite', site=name_of_website.site_name)

        websites = WebSites.objects.filter(user=request.user)
        proxy = Proxy.objects.filter(available=True)
        return render(request, 'main/vpn.html', {'title': 'VPN', 'proxy': proxy, 'websites': websites})
    else:
        return render(request, 'main/constant_templates/closed.html', {'title': 'closed_access'})


# ------------------------------------------------Choose page------------------------------------------------------

# -----------------------------------------------Frame with VPN-----------------------------------------------------
# this frame is used to show sites in the VPN
# !!!!!!!!!!!!!!!!!!!!!!
# VPN NOT CONNECTED YET
# !!!!!!!!!!!!!!!!!!!!!!!
def brows_vpn(request, site):
    if request.user.is_authenticated:
        # get dictionary of chosen proxy
        user_proxy = request.session.get('user_proxy')
        http = get_proxy_http(user_proxy)
        proxy_data = get_proxy_data(user_proxy)

        # get web site chosen by client
        link_target = WebSites.objects.get(site_name=site).site_url

        # data collecting
        request_size = len(request.body)
        response_size = len(requests.get(link_target).content)

        return render(request, 'main/vpn_view.html', {'title': 'VPN',
                                                      'link': link_target,
                                                      'proxy': proxy_data,
                                                      'http': http,
                                                      'request_size': request_size,
                                                      'response_size': response_size})
    else:
        return render(request, 'main/constant_templates/closed.html', {'title': 'closed_access'})

# -----------------------------------------------Frame with VPN-----------------------------------------------------