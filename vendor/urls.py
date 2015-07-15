from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^login/$', views.venderLogin, name='login'),
    url(r'^menu/$', views.venderMenu, name='menu'),
    url(r'^logout/$', views.venderLogout, name='logout'),
]
