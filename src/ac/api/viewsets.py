import logging

from rest_framework import viewsets
from vng_api_common.authorizations.models import Applicatie

from .filters import ApplicatieFilter
from .serializers import ApplicatieSerializer

# from vng_api_common.permissions import ActionScopesRequired


logger = logging.getLogger(__name__)


class ApplicatieViewSet(viewsets.ModelViewSet):
    queryset = Applicatie.objects.prefetch_related('autorisaties').order_by('-pk')
    serializer_class = ApplicatieSerializer
    filterset_class = ApplicatieFilter
    lookup_field = 'uuid'

    # permission_classes = (ActionScopesRequired,)
