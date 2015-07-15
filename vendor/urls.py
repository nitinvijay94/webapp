from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^login/$', views.venderLogin, name='login'),
    url(r'^menu/$', views.venderMenu, name='menu'),
    url(r'^logout/$', views.venderLogout, name='logout'),
]
