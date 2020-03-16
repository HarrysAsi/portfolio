from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from django.conf.urls.static import static
from portfolio import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("apps.root.urls")),
]

handler404 = "apps.root.views.handler404"
handler500 = "apps.root.views.handler500"

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
