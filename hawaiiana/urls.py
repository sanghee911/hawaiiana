from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # default urls
    url(r'^admin/', admin.site.urls),
    # third-party urls
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    # my sites urls
    url(r'^', include('home.urls')),
    url(r'^menu/', include('menu.urls', namespace='menu')),
    url(r'^location/', include('location.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
