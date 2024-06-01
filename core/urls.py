from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("api/v1/plants/", include("plant.urls")),
    path("api/v1/design/", include("design.urls")),
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
]

# Admin Site Config
admin.site.site_header = "Turbo School Management System"
admin.site.site_title = "Turbo School Management System"
admin.site.index_title = "Welcome to Turbo School Management System"


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # Django Debug Toolbar

    # import debug_toolbar

    # urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
