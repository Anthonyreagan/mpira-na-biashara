# mpiranabiashara/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings # NEW
from django.conf.urls.static import static # NEW

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('blog/', include('blog.urls')),
    path('services/', include('services.urls')),
    path('contact/', include('contact.urls')),
    path('team/', include('team.urls')),
]

# NEW: Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)