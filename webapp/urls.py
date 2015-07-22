from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from vendor import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'resid', views.ResIDViewSet)

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^vendor/', include('vendor.urls')),
                       url(r'^', include(router.urls)),
                       url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                       url(r'^search/', views.TagsView.as_view(), name='TagsView'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
