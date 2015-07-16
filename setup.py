# create user first
from django.contrib.auth.models import User

print User.objects.all()
User.objects.create_user('panda', 'panda@gatech.edu', 'panda')
User.objects.create_user('chickenfila', 'chickenfila@gatech.edu', 'chickenfila')

# create serveral rows in the table
from vendor.models import *

resid1 = ResID(name='panda')
resid1.save()
hours1 = Hours(name='panda')
hours1.save()
emptydish1 = Dish(name='', nextdish=None)
emptydish1.save()
dish1 = Dish(name='Chicken Sandwich', nextdish=emptydish1)
dish1.save()
dish2 = Dish(name='Spicy Sandwich', nextdish=dish1)
dish2.save()
menus1 = Menus(name='panda', firstdish=dish2, dishnum=3)
menus1.save()
usermap1 = UserMap(username='panda', resid=resid1, hours=hours1, menu=menus1)
usermap1.save()

resid2 = ResID(name='chickenfila')
resid2.save()
hours2 = Hours(name='chickenfila')
hours2.save()
emptydish2 =Dish(name='', nextdish=None)
emptydish2.save()
dish3 =Dish(name='Chicken Sandwich', nextdish=emptydish2)
dish3.save()
dish4 =Dish(name='Spicy Sandwich', nextdish=dish3)
dish4.save()
menus2 = Menus(name='chickenfila', firstdish=dish4, dishnum=3)
menus2.save()
usermap2 = UserMap(username='chickenfila', resid=resid2, hours=hours2, menu=menus2)
usermap2.save()

