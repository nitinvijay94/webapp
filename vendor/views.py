from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from rest_framework import viewsets
from .models import UserMap, ResID, Hours
from .forms import *
from . import serializers 
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


def updateDishes(formset, resid):
    allDishes = Dish.objects.filter(resid__exact=resid)
    allDishes.delete()          # first delete all existing entries
    for form in formset:        # then add new entries
        if form.cleaned_data['isdelete'] is False:
            mydish = Dish(name=form.cleaned_data['name'],
                          price=form.cleaned_data['price'],
                          calories=form.cleaned_data['calories'],
                          resid=resid)
            mydish.save()
            

def getFormSet(resid, addNum=0):
    allDishes = Dish.objects.filter(resid__exact=resid)
    data = []
    for dish in allDishes:
        data.append({'name': dish.name, 'price': dish.price, 'calories': dish.calories})
    for i in range(addNum):
        data.append({'name': "name", 'price': 0, 'calories': 0})

    dishFormSet = formset_factory(dishForm, extra=0)
    return dishFormSet(initial=data)


@login_required(login_url='login')
def vendorMenu(request):
    username = request.user.username  # get the login username
    usermap = UserMap.objects.get(username=username)  # get the table entry
    dishFormSet = formset_factory(dishForm, extra=0)

    if request.method == 'POST':

        ######################################################################
        #  actions taken when user change the menu
        if 'menulistSubmit' in request.POST:
            formset = dishFormSet(request.POST)
            if formset.is_valid():
                updateDishes(formset, usermap.resid)
                formset = getFormSet(usermap.resid)
            else:
                messages.error(request, "Error")
                
            return render(request, 'vendor/menu.html',
                          {'logoUrl': usermap.resid.logo.url,
                           'menuUrl': usermap.resid.menu.url,
                           'formhour': HourForm(instance=usermap.hours),
                           'formset': formset,
                           'formlogo': LogoForm(),
                           'formmenu': MenuForm(),
                           'formlocation': LocationForm(instance=usermap.loc)})

        ######################################################################
        #  actions taken when user change the logo
        if 'logoSubmit' in request.POST:
            formset = getFormSet(usermap.resid)
            formlogo = LogoForm(request.POST, request.FILES)
            if formlogo.is_valid():
                usermap.resid.logo = formlogo.cleaned_data['image']
                usermap.resid.save()
            else:
                messages.error(request, "Error")
            return render(request, 'vendor/menu.html',
                          {'logoUrl': usermap.resid.logo.url,
                           'menuUrl': usermap.resid.menu.url,
                           'formset': formset,
                           'formhour': HourForm(instance=usermap.hours),
                           'formlogo': LogoForm(),
                           'formmenu': MenuForm(),
                           'formlocation': LocationForm(instance=usermap.loc)})

        ######################################################################
        #  actions taken when user change the menu picture
        if 'menuSubmit' in request.POST:
            formset = getFormSet(usermap.resid)
            formmenu = MenuForm(request.POST, request.FILES)
            if formmenu.is_valid():
                usermap.resid.menu = formmenu.cleaned_data['image']
                usermap.resid.save()
            else:
                messages.error(request, "Error")
            return render(request, 'vendor/menu.html',
                          {'logoUrl': usermap.resid.logo.url,
                           'menuUrl': usermap.resid.menu.url,
                           'formset': formset,
                           'formhour': HourForm(instance=usermap.hours),
                           'formmenu': LogoForm(),
                           'formlogo': MenuForm(),
                           'formlocation': LocationForm(instance=usermap.loc)})

        ######################################################################
        #  actions taken when user change the hours
        if 'hoursSubmit' in request.POST:
            formset = getFormSet(usermap.resid)
            formhour = HourForm(request.POST)
            if formhour.is_valid():
                usermap.hours.open_time_m = formhour.cleaned_data['open_time_m']
                usermap.hours.close_time_m = formhour.cleaned_data['close_time_m']
                usermap.hours.open_time_t = formhour.cleaned_data['open_time_t']
                usermap.hours.close_time_t = formhour.cleaned_data['close_time_t']
                usermap.hours.open_time_w = formhour.cleaned_data['open_time_w']
                usermap.hours.close_time_w = formhour.cleaned_data['close_time_w']
                usermap.hours.open_time_r = formhour.cleaned_data['open_time_r']
                usermap.hours.close_time_r = formhour.cleaned_data['close_time_r']
                usermap.hours.open_time_f = formhour.cleaned_data['open_time_f']
                usermap.hours.close_time_f = formhour.cleaned_data['close_time_f']
                usermap.hours.open_time_s = formhour.cleaned_data['open_time_s']
                usermap.hours.close_time_s = formhour.cleaned_data['close_time_s']
                usermap.hours.open_time_h = formhour.cleaned_data['open_time_h']
                usermap.hours.close_time_h = formhour.cleaned_data['close_time_h']

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
            return render(request, 'vendor/menu.html',
                          {'logoUrl': usermap.resid.logo.url,
                           'menuUrl': usermap.resid.menu.url,
                           'formset': formset,
                           'formhour': HourForm(instance=usermap.hours),
                           'formlogo': LogoForm(),
                           'formmenu': MenuForm(),
                           'formlocation': LocationForm(instance=usermap.loc)})

        ######################################################################
        #  actions taken when user change the leftTime
        if 'leftTimeSubmit' in request.POST:
            formset = getFormSet(usermap.resid)
            formhour = HourForm(request.POST)
            if formhour.is_valid():
                usermap.hours.leftTime = formhour.cleaned_data['leftTime']
                usermap.hours.save()
            else:
                messages.error(request, "Error")
            return render(request, 'vendor/menu.html',
                          {'logoUrl': usermap.resid.logo.url,
                           'menuUrl': usermap.resid.menu.url,
                           'formset': formset,
                           'formhour': HourForm(instance=usermap.hours),
                           'formlogo': LogoForm(),
                           'formmenu': MenuForm(),
                           'formlocation': LocationForm(instance=usermap.loc)})
        
        ######################################################################
        #  actions taken when user add dish to the menu
        if 'addDishSubmit' in request.POST:
            formset = getFormSet(usermap.resid, 1)
            return render(request, 'vendor/menu.html',
                          {'logoUrl': usermap.resid.logo.url,
                           'menuUrl': usermap.resid.menu.url,
                           'formset': formset,
                           'formhour': HourForm(instance=usermap.hours),
                           'formlogo': LogoForm(),
                           'formmenu': MenuForm(),
                           'formlocation': LocationForm(instance=usermap.loc)})
        
        ######################################################################
        # actions taken when user update location
        if 'locSubmit' in request.POST:
            formset = getFormSet(usermap.resid)
            formloc = LocationForm(request.POST)
            if formloc.is_valid():
                usermap.loc.address = formloc.cleaned_data['address']
                usermap.loc.latitude = formloc.cleaned_data['latitude']
                usermap.loc.longitude = formloc.cleaned_data['longitude']
                usermap.loc.save()
            else:
                messages.error(request, "Error")

            return render(request, 'vendor/menu.html',
                          {'logoUrl': usermap.resid.logo.url,
                           'menuUrl': usermap.resid.menu.url,
                           'formset': formset,
                           'formhour': HourForm(instance=usermap.hours),
                           'formlogo': LogoForm(),
                           'formmenu': MenuForm(),
                           'formlocation': LocationForm(instance=usermap.loc)})

    ######################################################################
    # default GET behaviour
    formset = getFormSet(usermap.resid)
    print LocationForm(instance=usermap.loc)
    return render(request, 'vendor/menu.html',
                  {'logoUrl': usermap.resid.logo.url,
                   'menuUrl': usermap.resid.menu.url,
                   'formset': formset,
                   'formhour': HourForm(instance=usermap.hours),
                   'formlogo': LogoForm(),
                   'formmenu': MenuForm(),
                   'formlocation': LocationForm(instance=usermap.loc)})


######################################################################
#                        following : rest api part                   #
######################################################################

class ResIDViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = ResID.objects.all()
    serializer_class = serializers.ResIDSerializer

