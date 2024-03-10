from django.contrib import admin
from django.urls import path, include

from events.apps import LocationServiceConfig


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(
        ('events.api_urls', LocationServiceConfig.name),
        namespace='applications'
        )
    ),
]
