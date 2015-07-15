from django.db import models


class ResID(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='images/logo',
                             default='images/logo/logo_default.svg',
                             max_length=100)

    def __str__(self):
        return self.name


class UserMap(models.Model):
    username = models.CharField(max_length=100)
    resid = models.OneToOneField(ResID)

    def __str__(self):
        return self.username
