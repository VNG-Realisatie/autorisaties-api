import logging

from rest_framework import viewsets
# from vng_api_common.permissions import ActionScopesRequired

from vng_api_common.authorizations.models import Applicatie
from .serializers import ApplicatieSerializer

logger = logging.getLogger(__name__)


class ApplicatieViewSet(viewsets.ModelViewSet):
    queryset = Applicatie.objects.all()
    serializer_class = ApplicatieSerializer
    lookup_field = 'uuid'

    # permission_classes = (ActionScopesRequired,)
    # required_scopes = {
    #     'list': EXAMPLE_SCOPE,
    #     'retrieve': EXAMPLE_SCOPE,
    #     'create': EXAMPLE_SCOPE,
    #     'update': EXAMPLE_SCOPE,
    #     'partial_update': EXAMPLE_SCOPE,
    #     'destroy': EXAMPLE_SCOPE,
    # }
