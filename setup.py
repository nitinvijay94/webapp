from vendor.models import UserMap, ResID


resid1 = ResID(name='panda')
resid1.save()
usermap1 = UserMap(username='panda', resid=resid1)
usermap1.save()
