from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from lozapp.views import homepage

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^event/', include('lozapp.urls'), name="event"),
    url(r'^profile/', include('lozprofile.urls'), name="profile"),
    url(r'^$', homepage, name="home-page"),


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
