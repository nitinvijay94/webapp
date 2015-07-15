from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^vendor/', include('vendor.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

