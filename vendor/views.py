from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from rest_framework import viewsets
from .models import UserMap, ResID, Hours
from .forms import *
from .serializers import ResIDSerializer, HoursSerializer
from django.http import HttpResponse
from django.forms.formsets import formset_factory

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
def vendorMenu(request):
    username = request.user.username  # get the login username
    usermap = UserMap.objects.get(username=username)  # get the table entry
    dishFormSet = formset_factory(dishForm, extra=1)
    formlogo = LogoForm()
    formmenu = MenuForm()
    formhour = HourForm()
    formset = dishFormSet()

    if request.method == 'POST':

        ######################################################################
        #  actions taken when user change the menu
        if 'menulistSubmit' in request.POST:
            formset = dishFormSet(request.POST)
            if formset.is_valid():
                predish = usermap.menu.firstdish
                length=len(formset.cleaned_data)
                for index in range(0,length-1):
                    mydish = Dish(name="", price=0.0, calories=0.0, nextdish=None)
                    mydish.save()
                    predish.nextdish = mydish
                    mydish.name = formset.cleaned_data[index]['name']
                    mydish.price = formset.cleaned_data[index]['price']
                    mydish.calories = formset.cleaned_data[index]['calories']
                    predish = mydish
            else:
                messages.error(request, "Error")
            return render(request, 'vendor/menu.html', {'logoUrl':usermap.resid.logo.url, 'menuUrl': usermap.resid.menu.url, 'formhour':HourForm(instance=usermap.hours),  'formset': formset, 'formlogo':formlogo, 'formmenu':formmenu})

        ######################################################################
        #  actions taken when user change the logo
        if 'logoSubmit' in request.POST:
            formlogo = LogoForm(request.POST, request.FILES)
            if formlogo.is_valid():
                usermap.resid.logo = formlogo.cleaned_data['image']
                usermap.resid.save()
            else:
                messages.error(request, "Error")
            return render(request, 'vendor/menu.html', {'logoUrl': usermap.resid.logo.url, 'menuUrl': usermap.resid.menu.url, 'formhour':HourForm(instance=usermap.hours), 'formlogo': formlogo, 'formmenu':formmenu})

        ######################################################################
        #  actions taken when user change the menu picture
        if 'menuSubmit' in request.POST:
            formmenu = MenuForm(request.POST, request.FILES)
            if formmenu.is_valid():
                usermap.resid.menu = formmenu.cleaned_data['image']
                usermap.resid.save()
            else:
                messages.error(request, "Error")
            return render(request, 'vendor/menu.html', {'logoUrl': usermap.resid.logo.url, 'menuUrl': usermap.resid.menu.url, 'formhour':HourForm(instance=usermap.hours), 'formmenu': formmenu, 'formlogo':formlogo})

        ######################################################################
        #  actions taken when user change the hours
        if 'hoursSubmit' in request.POST:
            formhour = HourForm(request.POST)
            if formhour.is_valid():
                usermap.hours.open_time = formhour.cleaned_data['open_time']
                usermap.hours.close_time = formhour.cleaned_data['close_time']
                usermap.hours.m = formhour.cleaned_data['m']
                usermap.hours.t = formhour.cleaned_data['t']
                usermap.hours.w = formhour.cleaned_data['w']
                usermap.hours.r = formhour.cleaned_data['r']
                usermap.hours.f = formhour.cleaned_data['f']
                usermap.hours.s = formhour.cleaned_data['s']
                usermap.hours.h = formhour.cleaned_data['h']
                usermap.hours.save()
            else:
                messages.error(request, "Error")
            return render(request, 'vendor/menu.html', {'logoUrl': usermap.resid.logo.url, 'menuUrl': usermap.resid.menu.url, 'formhour': formhour, 'formlogo':formlogo, 'formmenu':formmenu})
        
    else:
        setlist=[]
        mydish=usermap.menu.firstdish
        for i in range(0,1000):
            if mydish.nextdish != None:
                setlist.append({'name': mydish.name, 'price': mydish.price, 'calories': mydish.calories})
                mydish=mydish.nextdish
            else:
                break
        formset = dishFormSet(initial=setlist)
        formlogo = LogoForm()
        formmenu = MenuForm()
        formhour = HourForm(instance=usermap.hours)
    return render(request, 'vendor/menu.html', {'logoUrl':usermap.resid.logo.url, 'menuUrl': usermap.resid.menu.url, 'formlogo':formlogo, 'formmenu':formmenu, 'formhour':formhour, 'formset': formset})


######################################################################
#                        following : rest api part                   #
######################################################################

class ResIDViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = ResID.objects.all()
    serializer_class = ResIDSerializer
