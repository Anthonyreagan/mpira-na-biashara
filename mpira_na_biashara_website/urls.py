# mybusinesswebsite/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')), # Core app URLs at the root
    path('blog/', include('blog.urls')), # Blog app URLs under /blog/
]