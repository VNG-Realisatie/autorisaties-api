import logging

from rest_framework import viewsets
from vng_api_common.authorizations.models import Applicatie
from vng_api_common.authorizations.serializers import ApplicatieSerializer
from vng_api_common.notifications.viewsets import NotificationViewSetMixin
from vng_api_common.permissions import AuthScopesRequired

from .filters import ApplicatieFilter
from .kanalen import KANAAL_AUTORISATIES
from .scopes import SCOPE_AUTORISATIES_BIJWERKEN, SCOPE_AUTORISATIES_LEZEN

logger = logging.getLogger(__name__)


class ApplicatieViewSet(NotificationViewSetMixin,
                        viewsets.ModelViewSet):

    queryset = Applicatie.objects.prefetch_related('autorisaties').order_by('-pk')
    serializer_class = ApplicatieSerializer
    filterset_class = ApplicatieFilter
    lookup_field = 'uuid'
    permission_classes = (AuthScopesRequired,)
    required_scopes = {
        'list': SCOPE_AUTORISATIES_LEZEN,
        'retrieve': SCOPE_AUTORISATIES_LEZEN,
        'create': SCOPE_AUTORISATIES_BIJWERKEN,
        'destroy': SCOPE_AUTORISATIES_BIJWERKEN,
        'update': SCOPE_AUTORISATIES_BIJWERKEN,
        'partial_update': SCOPE_AUTORISATIES_BIJWERKEN,
    }
    notifications_kanaal = KANAAL_AUTORISATIES
