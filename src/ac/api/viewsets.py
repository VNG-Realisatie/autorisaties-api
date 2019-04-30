import logging

from rest_framework import viewsets
from vng_api_common.authorizations.models import Applicatie
from vng_api_common.authorizations.serializers import ApplicatieSerializer
from vng_api_common.notifications.viewsets import NotificationViewSetMixin

from .filters import ApplicatieFilter
from .kanalen import KANAAL_AUTORISATIES

logger = logging.getLogger(__name__)


class ApplicatieViewSet(NotificationViewSetMixin,
                        viewsets.ModelViewSet):

    queryset = Applicatie.objects.prefetch_related('autorisaties').order_by('-pk')
    serializer_class = ApplicatieSerializer
    filterset_class = ApplicatieFilter
    lookup_field = 'uuid'

    notifications_kanaal = KANAAL_AUTORISATIES
