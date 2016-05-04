from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from lozapp.views import homepage

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^event/', include('lozapp.urls')),
    url(r'^profile/', include('lozprofile.urls')),
    url(r'^$', homepage),


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
