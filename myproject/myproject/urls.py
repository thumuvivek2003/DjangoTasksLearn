from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls')),
    path('bookapp/', include('mybookapp.urls')),
    path('accounts/', include('accounts.urls')),
    path('', include('django.contrib.auth.urls')), 
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
