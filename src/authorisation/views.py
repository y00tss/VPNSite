
from django.contrib.auth import login
from django.db.models import Count
from django.shortcuts import render, redirect
from authorisation.form import SignUpForm, ProfileEditForm
from main.models import SiteAttended, WebSites


# -----------------------------------------Registration and authorisation-----------------------------------------------

# special page for closed access for who is not logged in
def closed_access(request):
    return render(request, 'main/constant_templates/closed.html', {'title': 'closed_access'})


# page for registration
def singup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = SignUpForm()
    return render(request, 'registration/registration.html', {'form': form, 'title': 'Registration'})


# -----------------------------------------Registration and authorisation-----------------------------------------------

# ---------------------------------------------------USER PAGES---------------------------------------------------------

# profile page
def profile_view(request):
    if request.user.is_authenticated:
        attended = SiteAttended.objects.filter(user=request.user) \
            .values('site__site_name') \
            .annotate(click_count=Count('site'))
        websites = WebSites.objects.filter(user=request.user)
        return render(request, 'authorisation/profile.html', {'title': 'Profile',
                                                              'websites': websites,
                                                              'attended': attended})
    else:
        return render(request, 'main/constant_templates/closed.html', {'title': 'closed_access'})


# edit profile page
def edit_profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ProfileEditForm(request.POST, request.FILES, instance=request.user)
            if form.is_valid():
                form.save()
                return redirect('profile')
        else:
            form = ProfileEditForm(instance=request.user)
        return render(request, 'authorisation/editprofile.html', {'form': form, 'title': 'Edit profile'})
    else:
        return render(request, 'main/constant_templates/closed.html', {'title': 'closed_access'})

# ---------------------------------------------------USER PAGES---------------------------------------------------------
