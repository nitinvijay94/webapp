from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import UserMap
from .forms import LogoImageForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def venderLogin(request):
    state = ""
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"
                return HttpResponseRedirect(reverse('menu'))
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."

    return render(request, 'vendor/login.html', {'state': state, 'username': username})


def venderLogout(request):
    logout(request)
    return render(request, 'vendor/logout.html')


@login_required(login_url='login')
def venderMenu(request):
    username = request.user.username  # get the login username
    usermap = UserMap.objects.get(username=username)  # get the table entry
    if request.method == 'POST':
        if 'logoSubmit' in request.POST:
            form = LogoImageForm(request.POST, request.FILES)
            if form.is_valid():
                usermap.resid.logo = form.cleaned_data['image']
                usermap.resid.save()
            else:
                messages.error(request, "Error")
        return render(request, 'vendor/menu.html', {'logoUrl': usermap.resid.logo.url, 'form': form})
    else:
        form = LogoImageForm()

    print usermap.resid.logo.url
    return render(request, 'vendor/menu.html', {'logoUrl': usermap.resid.logo.url, 'form': form})
