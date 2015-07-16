# create user first
from django.contrib.auth.models import User

print User.objects.all()
User.objects.create_user('panda', 'panda@gatech.edu', 'panda')
User.objects.create_user('chickenfila', 'chickenfila@gatech.edu', 'chickenfila')

# create serveral rows in the table
from vendor.models import UserMap, ResID, Hours

resid1 = ResID(name='panda')
resid1.save()
hours1 = Hours(name='panda')
hours1.save()
usermap1 = UserMap(username='panda', resid=resid1, hours=hours1)
usermap1.save()

resid2 = ResID(name='chickenfila')
resid2.save()
hours2 = Hours(name='chickenfila')
hours2.save()
usermap2 = UserMap(username='chickenfila', resid=resid2, hours=hours2)
usermap2.save()
