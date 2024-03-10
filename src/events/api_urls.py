from rest_framework import routers

from .api_views import SpaceCraftViewset

router = routers.SimpleRouter()
router.register(r'events', SpaceCraftViewset)

urlpatterns = router.urls
