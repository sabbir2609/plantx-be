from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("api/", include("main.urls")),
    path("", include("blog.urls")),
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
]

# Admin Site Config
admin.site.site_header = "Viriditas Admin"
admin.site.site_title = "Viriditas"
admin.site.index_title = "Welcome to Viriditas Administration"


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
