"""
Views for authorisation app
"""
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import render, redirect
from authorisation.form import SignUpForm, ProfileEditForm
from main.models import SiteAttended, WebSites
from main.service import create_proxy


def closed_access(request):
    """View for closed access page"""
    return render(
        request,
        'main/constant_templates/closed.html',
        {'title': 'closed_access'},
    )


def singup(request):
    """View for registration page"""
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # fill up proxy database for testing with first registration
            create_proxy()
            return redirect('profile')
    else:
        form = SignUpForm()
    return render(
        request,
        'registration/registration.html',
        {'form': form, 'title': 'Registration'},
    )


@login_required
def profile_view(request):
    """View for profile page"""
    if request.user.is_authenticated:
        attended = SiteAttended.objects.filter(user=request.user) \
            .values('site__site_name') \
            .annotate(click_count=Count('site'))
        websites = WebSites.objects.filter(user=request.user)
        return render(
            request,
            'authorisation/profile.html',
            {'title': 'Profile',
             'websites': websites,
             'attended': attended,
             }
        )
    else:
        return render(
            request,
            'main/constant_templates/closed.html',
            {'title': 'closed_access'},
        )


@login_required
def edit_profile(request):
    """View for edit profile page"""
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ProfileEditForm(request.POST, request.FILES, instance=request.user)  # noqa
            if form.is_valid():
                form.save()
                return redirect('profile')
        else:
            form = ProfileEditForm(instance=request.user)
        return render(
            request,
            'authorisation/editprofile.html',
            {'form': form, 'title': 'Edit profile'},
        )
    else:
        return render(
            request,
            'main/constant_templates/closed.html',
            {'title': 'closed_access'},
        )
