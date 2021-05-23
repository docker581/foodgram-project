from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

handler404 = "data.views.page_not_found" 
handler500 = "data.views.server_error"

urlpatterns = [
    path("auth/", include("users.urls")),
    path("auth/", include("django.contrib.auth.urls")),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', include('data.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root=settings.MEDIA_ROOT,
    )
    urlpatterns += static(
        settings.STATIC_URL, 
        document_root=settings.STATIC_ROOT,
    )
