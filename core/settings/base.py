from datetime import timedelta
import os
from pathlib import Path

from django.templatetags.static import static
from django.urls import reverse_lazy  # noqa: F401
from django.utils.translation import gettext_lazy as _  # noqa: F401
from import_export.formats.base_formats import XLSX, CSV, JSON

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Application definition
INSTALLED_APPS = [
    # unfold
    "unfold",  # before django.contrib.admin
    "unfold.contrib.filters",  # optional, if special filters are needed
    "unfold.contrib.forms",  # optional, if special form elements are needed
    "unfold.contrib.inlines",  # optional, if special inlines are needed
    "unfold.contrib.import_export",  # for django-import-export
    # django apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "cloudinary_storage",
    "cloudinary",
    # my apps
    "main",
    "home",
    "zone",
    "tags",
    "users",
    "decouple",
    # third-party apps
    "corsheaders",
    "rest_framework",
    "djoser",
    "django_filters",
    "import_export",
    # debug toolbar
    "debug_toolbar",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # whitenoise middleware
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "corsheaders.middleware.CorsMiddleware",  # cors middleware
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",  # debug toolbar middleware
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Dhaka"

USE_I18N = True

USE_TZ = True

LANGUAGES = [
    ("en", _("English")),
    ("bn", _("Bangla")),
]

# Static files (CSS, JavaScript, Images)
STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


AUTHENTICATION_BACKENDS = [
    "users.backends.EmailAndUsernameBackend",  # custom backend for email and username login
    "social_core.backends.facebook.FacebookOAuth2",
    "social_core.backends.google.GoogleOAuth2",
    "django.contrib.auth.backends.ModelBackend",
]

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticatedOrReadOnly",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": ("users.authentication.CustomJWTAuthentication",),
    # "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

AUTH_USER_MODEL = "users.User"

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=3),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=10),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "UPDATE_LAST_LOGIN": False,
}

DJOSER = {
    "LOGIN_FIELD": "email",
    "USER_CREATE_PASSWORD_RETYPE": True,
    "ACTIVATION_URL": "auth/activation/{uid}/{token}",
    "SEND_ACTIVATION_EMAIL": True,
    "SEND_CONFIRMATION_EMAIL": True,
    "PASSWORD_CHANGED_EMAIL_CONFIRMATION": True,
    "PASSWORD_RESET_CONFIRM_URL": "auth/password-reset/{uid}/{token}",
    "SET_PASSWORD_RETYPE": True,
    "PASSWORD_RESET_SHOW_EMAIL_NOT_FOUND": True,
    "TOKEN_MODEL": None,
    "SERIALIZERS": {
        "user_create": "users.serializers.UserCreateSerializer",
        "users": "users.serializers.UserCreateSerializer",
        "user_delete": "djoser.serializers.UserDeleteSerializer",
    },
    "SOCIAL_AUTH_ALLOWED_REDIRECT_URIS": os.getenv("REDIRECT_URLS", "").split(","),
}


AUTH_COOKIE = "access"
AUTH_COOKIE_MAX_AGE = 60 * 60 * 24
AUTH_COOKIE_SECURE = os.getenv("AUTH_COOKIE_SECURE", "True") == "True"
AUTH_COOKIE_HTTP_ONLY = True
AUTH_COOKIE_PATH = "/"
AUTH_COOKIE_SAMESITE = "None"

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.getenv("GOOGLE_AUTH_KEY")
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.getenv("GOOGLE_AUTH_SECRET_KEY")
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    "https://www.googleapis.com/auth/userinfo.email",
    "https://www.googleapis.com/auth/userinfo.profile",
    "openid",
]

SOCIAL_AUTH_GOOGLE_OAUTH2_EXTRA_DATA = ["username"]

SOCIAL_AUTH_FACEBOOK_KEY = os.getenv("FACEBOOK_AUTH_KEY")
SOCIAL_AUTH_FACEBOOK_SECRET = os.getenv("FACEBOOK_AUTH_SECRET_KEY")

SOCIAL_AUTH_FACEBOOK_SCOPE = ["email"]
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {"fields": "email, first_name, last_name"}

DEFAULT_IMAGE = "image_not_found.webp"

UNFOLD = {
    "SITE_TITLE": "Viriditas",
    "SITE_HEADER": "Viriditas Admin",
    "SITE_SYMBOL": "home",
    "SITE_FAVICONS": [
        {
            "rel": "icon",
            "sizes": "32x32",
            "type": "image/svg+xml",
            "href": lambda request: static("favicon.ico"),
        },
    ],
    "SHOW_HISTORY": True,  # show/hide "History" button, default: True
    "TABS": [
        {
            "models": ["main.Customer", "main.Promotion"],
            "items": [
                {
                    "title": _("Customers"),
                    "icon": "person",
                    "link": reverse_lazy("admin:main_customer_changelist"),
                },
                {
                    "title": _("Promotions"),
                    "icon": "local_offer",
                    "link": reverse_lazy("admin:main_promotion_changelist"),
                },
            ],
        },
        {
            "models": ["main.PlantCategory", "main.Plant"],
            "items": [
                {
                    "title": _("Plant Categories"),
                    "icon": "category",
                    "link": reverse_lazy("admin:main_plantcategory_changelist"),
                },
                {
                    "title": _("Plants"),
                    "icon": "nature",
                    "link": reverse_lazy("admin:main_plant_changelist"),
                },
            ],
        },
        {
            "models": [
                "main.PlanterCategory",
                "main.Planter",
                "main.PlantingAccessoriesCategory",
                "main.PlantingAccessories",
            ],
            "items": [
                {
                    "title": _("Planter Categories"),
                    "icon": "category",
                    "link": reverse_lazy("admin:main_plantercategory_changelist"),
                },
                {
                    "title": _("Planters"),
                    "icon": "spa",
                    "link": reverse_lazy("admin:main_planter_changelist"),
                },
                {
                    "title": _("Accessories Categories"),
                    "icon": "category",
                    "link": reverse_lazy(
                        "admin:main_plantingaccessoriescategory_changelist"
                    ),
                },
                {
                    "title": _("Accessories"),
                    "icon": "build",
                    "link": reverse_lazy("admin:main_plantingaccessories_changelist"),
                },
            ],
        },
        {
            "models": ["auth.User", "auth.Group"],
            "items": [
                {
                    "title": _("Users"),
                    "icon": "person",
                    "link": reverse_lazy("admin:users_user_changelist"),
                },
                {
                    "title": _("Groups"),
                    "icon": "group",
                    "link": reverse_lazy("admin:auth_group_changelist"),
                },
            ],
        },
        {
            "models": ["zone.Zone", "tags.Tag"],
            "items": [
                {
                    "title": _("Zones"),
                    "icon": "map",
                    "link": reverse_lazy("admin:zone_zone_changelist"),
                },
                {
                    "title": _("Tags"),
                    "icon": "label",
                    "link": reverse_lazy("admin:tags_tag_changelist"),
                },
            ],
        },
    ],
    "SIDEBAR": {
        "show_search": True,  # Search in applications and models names
        "show_all_applications": True,  # Dropdown with all applications and models
        "navigation": [
            {
                "title": _("Navigation"),
                "items": [
                    {
                        "title": _("Dashboard"),
                        "icon": "dashboard",
                        "link": reverse_lazy("admin:index"),
                    },
                    {
                        "title": _("Customers"),
                        "icon": "person",
                        "link": reverse_lazy("admin:main_customer_changelist"),
                    },
                    {
                        "title": _("Promotions"),
                        "icon": "local_offer",
                        "link": reverse_lazy("admin:main_promotion_changelist"),
                    },
                ],
            },
            {
                "separator": True,
                "items": [
                    {
                        "title": _("Plant Categories"),
                        "icon": "category",
                        "link": reverse_lazy("admin:main_plantcategory_changelist"),
                    },
                    {
                        "title": _("Plants"),
                        "icon": "nature",
                        "link": reverse_lazy("admin:main_plant_changelist"),
                    },
                ],
            },
            {
                "separator": True,
                "items": [
                    {
                        "title": _("Planter Categories"),
                        "icon": "category",
                        "link": reverse_lazy("admin:main_plantercategory_changelist"),
                    },
                    {
                        "title": _("Planters"),
                        "icon": "spa",
                        "link": reverse_lazy("admin:main_planter_changelist"),
                    },
                    {
                        "title": _("Accessories Categories"),
                        "icon": "category",
                        "link": reverse_lazy(
                            "admin:main_plantingaccessoriescategory_changelist"
                        ),
                    },
                    {
                        "title": _("Accessories"),
                        "icon": "build",
                        "link": reverse_lazy(
                            "admin:main_plantingaccessories_changelist"
                        ),
                    },
                ],
            },
            {
                "separator": True,
                "items": [
                    {
                        "title": _("Users"),
                        "icon": "person",
                        "link": reverse_lazy("admin:users_user_changelist"),
                    },
                    {
                        "title": _("Groups"),
                        "icon": "group",
                        "link": reverse_lazy("admin:auth_group_changelist"),
                    },
                ],
            },
            {
                "separator": True,
                "items": [
                    {
                        "title": _("Zones"),
                        "icon": "map",
                        "link": reverse_lazy("admin:zone_zone_changelist"),
                    },
                    {
                        "title": _("Tags"),
                        "icon": "label",
                        "link": reverse_lazy("admin:tags_tag_changelist"),
                    },
                ],
            },
        ],
    },
}


IMPORT_EXPORT_FORMATS = [
    XLSX,
    CSV,
    JSON,
]
