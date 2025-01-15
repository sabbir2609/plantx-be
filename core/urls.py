from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

# dev import
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from home.views import HomePageTemplateView

urlpatterns = [
    path("", HomePageTemplateView.as_view(), name="home"),
    path("api/main/", include("main.urls"), name="main"),
    path("api/home/", include("home.urls")),
    path("api/blog/", include("blog.urls")),
    path("mail/", include("mailer.urls")),
    path("api/track/", include("tracker.urls")),
    path("api/auth/", include("users.urls"), name="users"),
    path("admin/", admin.site.urls),
    # path("api-auth/", include("rest_framework.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns.extend(
    [
        path("summernote/", include("django_summernote.urls")),
    ]
)


# Admin Site Config
admin.site.site_header = "Viriditas Admin"
admin.site.site_title = "Viriditas"
admin.site.index_title = "Welcome to Viriditas Administration"

if settings.DEBUG:
    from debug_toolbar.toolbar import debug_toolbar_urls

    urlpatterns += debug_toolbar_urls()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# dev
if settings.DEBUG:
    urlpatterns += [
        path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
        path(
            "api/schema/swagger-ui/",
            SpectacularSwaggerView.as_view(url_name="schema"),
            name="swagger-ui",
        ),
        path(
            "api/schema/redoc/",
            SpectacularRedocView.as_view(url_name="schema"),
            name="redoc",
        ),
    ]
