from django.db import models


class Hours(models.Model):
    open_time = models.TimeField(default='8:00')
    close_time = models.TimeField(default='20:00')
    m = models.BooleanField(default=True)
    t = models.BooleanField(default=True)
    w = models.BooleanField(default=True)
    r = models.BooleanField(default=True)
    f = models.BooleanField(default=True)
    s = models.BooleanField(default=False)
    h = models.BooleanField(default=False)
    leftTime = models.TimeField(blank=True, default='1:00')  # only works for food truck

    def __str__(self):
        return self.open_time


class ResID(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logo/',
                             default='logo/PandaLogo.png',
                             max_length=60)
    menu = models.ImageField(upload_to='menu/',
                             default='menu/pandamenu.jpeg',
                             max_length=200)
    
    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(default="7.00")
    calories = models.FloatField(default="100.00")
    resid = models.ForeignKey(ResID)

    def __str__(self):
        return self.name


class Location(models.Model):
    address = models.CharField(max_length=100)

    # latitude and longitude in degrees
    # the default value is the poition of Atlanta
    latitude = models.FloatField(default="33.7")
    longitude = models.FloatField(default="-84.4")

    def __str__(self):
        return self.address


class UserMap(models.Model):
    username = models.CharField(max_length=100)
    resid = models.OneToOneField(ResID)
    hours = models.OneToOneField(Hours)
    loc = models.OneToOneField(Location)

    def __str__(self):
        return self.username
