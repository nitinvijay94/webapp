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
    if request.method == 'POST':
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
            return render(request, 'vendor/menu.html', {'logoUrl':usermap.resid.logo.url, 'menuUrl': usermap.resid.menu.url, 'form':OneForm(), 'formset': formset})
        if 'logoSubmit' in request.POST:
            form = OneForm(request.POST, request.FILES)
            if form.is_valid():
                usermap.resid.logo = form.cleaned_data['image1']
                usermap.resid.save()
            else:
                messages.error(request, "Error")
            return render(request, 'vendor/menu.html', {'logoUrl': usermap.resid.logo.url, 'menuUrl': usermap.resid.menu.url, 'form': form})
        if 'menuSubmit' in request.POST:
            form = OneForm(request.POST, request.FILES)
            if form.is_valid():
                usermap.resid.menu = form.cleaned_data['image2']
                usermap.resid.save()
            else:
                messages.error(request, "Error")
            return render(request, 'vendor/menu.html', {'logoUrl': usermap.resid.logo.url, 'menuUrl': usermap.resid.menu.url, 'form': form})
        if 'hoursSubmit' in request.POST:
            form = OneForm(request.POST)
            if form.is_valid():
                usermap.hours.open_time = form.cleaned_data['opentime']
                usermap.hours.close_time = form.cleaned_data['closetime']
                usermap.hours.m = form.cleaned_data['d1']
                usermap.hours.t = form.cleaned_data['d2']
                usermap.hours.w = form.cleaned_data['d3']
                usermap.hours.r = form.cleaned_data['d4']
                usermap.hours.f = form.cleaned_data['d5']
                usermap.hours.s = form.cleaned_data['d6']
                usermap.hours.h = form.cleaned_data['d7']
                usermap.hours.save()
            else:
                messages.error(request, "Error")
            return render(request, 'vendor/menu.html', {'opentime': usermap.hours.open_time, 'closetime': usermap.hours.close_time, 
                                                        'd1': usermap.hours.m,
                                                        'd2': usermap.hours.t,
                                                        'd3': usermap.hours.w,
                                                        'd4': usermap.hours.r,
                                                        'd5': usermap.hours.f,
                                                        'd6': usermap.hours.s,
                                                        'd7': usermap.hours.h,
                                                        'form': form})
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
        form = OneForm()
    return render(request, 'vendor/menu.html', {'logoUrl':usermap.resid.logo.url, 'menuUrl': usermap.resid.menu.url, 'form':form, 'formset': formset})
 

######################################################################
#                        following : rest api part                   #
######################################################################

class ResIDViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = ResID.objects.all()
    serializer_class = ResIDSerializer
