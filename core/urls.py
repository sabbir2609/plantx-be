from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from home.views import HomePageTemplateView

urlpatterns = [
    path("", HomePageTemplateView.as_view(), name="home"),
    path("api/main/", include("main.urls")),
    path("api/home/", include("home.urls")),
    path("admin/", admin.site.urls),
    path("auth/", include("users.urls"), name="users"),
    # path("api-auth/", include("rest_framework.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Admin Site Config
admin.site.site_header = "Viriditas Admin"
admin.site.site_title = "Viriditas"
admin.site.index_title = "Welcome to Viriditas Administration"

if settings.DEBUG:
    from debug_toolbar.toolbar import debug_toolbar_urls

    urlpatterns += debug_toolbar_urls()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
