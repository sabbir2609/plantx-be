from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from home.views import HomePageTemplateView


urlpatterns = [
    path("", HomePageTemplateView.as_view(), name="home"),
    path("api/main/", include("main.urls")),
    path("api/home/", include("home.urls")),
    path("admin/", admin.site.urls),
    # path("api-auth/", include("rest_framework.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Admin Site Config
admin.site.site_header = "Viriditas Admin"
admin.site.site_title = "Viriditas"
admin.site.index_title = "Welcome to Viriditas Administration"


urlpatterns.extend(
    [
        path("ckeditor/", include("ckeditor_uploader.urls")),
    ]
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
