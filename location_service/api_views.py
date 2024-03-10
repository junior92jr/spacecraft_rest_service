from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from rest_framework.pagination import PageNumberPagination

from .models import Event
from .serializers import EventSerializer


class StandardResultsSetPagination(PageNumberPagination):
    """Class that defines pagination functionality."""

    page_size = 10
    page_size_query_param = 'page_size'


class SpaceCraftViewset(mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
    """Viewset that handles read operations."""

    queryset = Event.objects.all().order_by('event_identifier')
    serializer_class = EventSerializer
    permission_classes = (AllowAny,)
    lookup_field = 'event_identifier'
    pagination_class = StandardResultsSetPagination
