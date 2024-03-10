from django.contrib import admin
from django.urls import path, include

from location_service.apps import LocationServiceConfig

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(
        ('location_service.api_urls', LocationServiceConfig.name),
        namespace='applications'
        )
    ),
]
