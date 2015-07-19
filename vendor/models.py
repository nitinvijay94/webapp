from django.db import models


class Hours(models.Model):
    open_time_m = models.TimeField(blank=True, default='8:00')
    close_time_m = models.TimeField(blank=True, default='20:00')
    open_time_t = models.TimeField(blank=True, default='8:00')
    close_time_t = models.TimeField(blank=True, default='20:00')
    open_time_w = models.TimeField(blank=True, default='8:00')
    close_time_w = models.TimeField(blank=True, default='20:00')
    open_time_r = models.TimeField(blank=True, default='8:00')
    close_time_r = models.TimeField(blank=True, default='20:00')
    open_time_f = models.TimeField(blank=True, default='8:00')
    close_time_f = models.TimeField(blank=True, default='20:00')
    open_time_s = models.TimeField(blank=True, default='8:00')
    close_time_s = models.TimeField(blank=True, default='20:00')
    open_time_h = models.TimeField(blank=True, default='8:00')
    close_time_h = models.TimeField(blank=True, default='20:00')

    m = models.BooleanField(blank=True, default=True)
    t = models.BooleanField(blank=True, default=True)
    w = models.BooleanField(blank=True, default=True)
    r = models.BooleanField(blank=True, default=True)
    f = models.BooleanField(blank=True, default=True)
    s = models.BooleanField(blank=True, default=False)
    h = models.BooleanField(blank=True, default=False)
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
    resid = models.ForeignKey(ResID, related_name="dishes")

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
    resid = models.OneToOneField(ResID, related_name="usermap")
    hours = models.OneToOneField(Hours, related_name="usermap")
    loc = models.OneToOneField(Location, related_name="usermap")

    def __str__(self):
        return self.username
