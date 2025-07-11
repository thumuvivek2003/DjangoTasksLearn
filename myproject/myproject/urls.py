from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls')),
    path('bookapp/', include('mybookapp.urls')),
    path('accounts/', include('accounts.urls')),
    path('', include('django.contrib.auth.urls')), 
]
