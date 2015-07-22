import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'webapp.settings'

from django.contrib.auth.models import User
from vendor.models import *

from urllib import urlopen
import json
"""
def dumpclean(obj):
    if type(obj) == dict:
        for k, v in obj.items():
            if hasattr(v, '__iter__'):
                print k
                dumpclean(v)
            else:
                print '%s : %s' % (k, v)
    elif type(obj) == list:
        for v in obj:
            if hasattr(v, '__iter__'):
                dumpclean(v)
            else:
                print v
    else:
        print obj

"""
url = urlopen("http://test-diningdata.itg.gatech.edu:80/api/DiningLocations").read()
info = json.loads(url)
#dumpclean(result)""

for rest in info:
    user = rest["Name"].replace("(","")
    user = user.replace(")","")
    password = rest["Name"].split(' ')[0]
    tags = ""
    for tag in rest["Tags"]:
        tags = tags + "#" + tag["Name"]

    #Default username is name of restaurant without brackets and password is first word of Restaurant
    User.objects.create_user( user , password+'@gatech.edu', password)
    #Default Logo and Menu is the starbucks one for now
    description = rest["Description"]
    if description == None:
        description = ""
    resid = ResID(name=rest["Name"], description=description, logo='logo/starbuckslogo.png', menu='menu/starbucksmenu.jpg', tags=tags)
    resid.save()

    open_time_m = '8:00'
    close_time_m = '20:00'
    open_time_t = '8:00'
    close_time_t = '20:00'
    open_time_w = '8:00'
    close_time_w = '20:00'
    open_time_r = '8:00'
    close_time_r = '20:00'
    open_time_f = '8:00'
    close_time_f = '20:00'
    open_time_s = '8:00'
    close_time_s = '20:00'
    open_time_h = '8:00'
    close_time_h = '20:00'
    m = False 
    t = False
    w = False
    r = False
    f = False
    s = False
    h = False
    for dictHours in rest["HoursOfOperations"]:
        if dictHours["Close"]["Day"]==1:
            open_time_m = dictHours["Open"]["Time"]
            close_time_m = dictHours["Close"]["Time"]
            m = True
        elif dictHours["Close"]["Day"]==2:
            open_time_t = dictHours["Open"]["Time"]
            close_time_t = dictHours["Close"]["Time"]
            t = True
        elif dictHours["Close"]["Day"]==3:
            open_time_w = dictHours["Open"]["Time"]
            close_time_w = dictHours["Close"]["Time"]
            w = True
        elif dictHours["Close"]["Day"]==4:
            open_time_r = dictHours["Open"]["Time"]
            close_time_r = dictHours["Close"]["Time"]
            r = True
        elif dictHours["Close"]["Day"]==5:
            open_time_f = dictHours["Open"]["Time"]
            close_time_f = dictHours["Close"]["Time"]
            f = True
        elif dictHours["Close"]["Day"]==6:
            open_time_s = dictHours["Open"]["Time"]
            close_time_s = dictHours["Close"]["Time"]
            s = True
        elif dictHours["Close"]["Day"]==7:
            open_time_h = dictHours["Open"]["Time"]
            close_time_h = dictHours["Close"]["Time"]
            h = True

    hours = Hours(open_time_m=open_time_m, close_time_m=close_time_m,
                  open_time_t=open_time_t, close_time_t=close_time_t,
                  open_time_w=open_time_w, close_time_w=close_time_w,
                  open_time_r=open_time_r, close_time_r=close_time_r,
                  open_time_f=open_time_f, close_time_f=close_time_f,
                  open_time_s=open_time_s, close_time_s=close_time_s,
                  open_time_h=open_time_h, close_time_h=close_time_h,
                  m=m, t=t, w=w, r=r, f=f, s=s, h=h)
    hours.save()


    details = rest["LocationDetails"]
    if details == None:
        details = ""
    loc = Location(address="",  details=details, latitude=rest["Latitude"], longitude=rest["Longitude"])
    loc.save()

    usermap = UserMap(username=user, resid=resid, hours=hours, loc=loc)
    usermap.save()
