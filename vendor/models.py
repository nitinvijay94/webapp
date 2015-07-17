from django.db import models

class Hours(models.Model):
    name = models.CharField(max_length=100)
    open_time = models.TimeField(default = '8:00')
    close_time = models.TimeField(default = '20:00')
    m = models.BooleanField(default = False )
    t = models.BooleanField(default = False )
    w = models.BooleanField(default = False )
    r = models.BooleanField(default = False )
    f = models.BooleanField(default = False )
    s = models.BooleanField(default = False )
    h = models.BooleanField(default = False )

    def __str__(self):
        return self.name


class Menus(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


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


class UserMap(models.Model):
    username = models.CharField(max_length=100)
    resid = models.OneToOneField(ResID)
    hours = models.OneToOneField(Hours)
    menu = models.OneToOneField(Menus)

    def __str__(self):
        return self.username
