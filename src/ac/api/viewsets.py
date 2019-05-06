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


class ApplicatieViewSet(NotificationViewSetMixin, viewsets.ModelViewSet):
    """
    Uitlezen en configureren van autorisaties voor applicaties.

    list:
    Geef een collectie van applicaties, met ingesloten autorisaties.

    De autorisaties zijn gedefinieerd op een specifieke component, bijvoorbeeld
    het ZRC, en geven aan welke scopes van toepassing zijn voor dit component.
    De waarde van de `component` bepaalt ook welke verdere informatie ingesloten
    is, zoals `zaaktype` en `maxVertrouwelijkheidaanduiding` voor het ZRC.

    In dit voorbeeld gelden er dus zaaktype-specifieke scopes en mogen zaken
    van het betreffende zaaktype met een striktere vertrouwelijkheidaanduiding
    dan `maxVertrouwelijkheidaanduiding` niet ontsloten worden.

    De collectie kan doorzocht worden met de ``clientIds`` query parameter.

    retrieve:
    Vraag een applicatie op, met ingesloten autorisaties.

    De autorisaties zijn gedefinieerd op een specifieke component, bijvoorbeeld
    het ZRC, en geven aan welke scopes van toepassing zijn voor dit component.
    De waarde van de `component` bepaalt ook welke verdere informatie ingesloten
    is, zoals `zaaktype` en `maxVertrouwelijkheidaanduiding` voor het ZRC.

    In dit voorbeeld gelden er dus zaaktype-specifieke scopes en mogen zaken
    van het betreffende zaaktype met een striktere vertrouwelijkheidaanduiding
    dan `maxVertrouwelijkheidaanduiding` niet ontsloten worden.

    create:
    Registreer een applicatie met een bepaalde set van autorisaties.

    Indien `heeftAlleAutorisaties` gezet is, dan moet je
    `autorisaties` leeg (of weg) laten.

    Indien je `autorisaties` meegeeft, dan moet `heeftAlleAutorisaties` de
    waarde `false` hebben of weggelaten worden.

    Na het aanmaken wordt een notificatie verstuurd.

    update:
    Werk de applicatie bij.

    Indien `heeftAlleAutorisaties` gezet is, dan moet je
    `autorisaties` leeg (of weg) laten.

    Indien je `autorisaties` meegeeft, dan moet `heeftAlleAutorisaties` de
    waarde `false` hebben of weggelaten worden.

    Na het bijwerken wordt een notificatie verstuurd.

    partial_update:
    Werk (een deel van) de applicatie bij.

    Indien `autorisaties` meegegeven is, dan worden de bestaande `autorisaties`
    vervangen met de nieuwe set van `autorisaties`.

    Indien `heeftAlleAutorisaties` gezet is, dan moet je
    `autorisaties` leeg (of weg) laten.

    Indien je `autorisaties` meegeeft, dan moet `heeftAlleAutorisaties` de
    waarde `false` hebben of weggelaten worden.

    Na het bijwerken wordt een notificatie verstuurd.

    destroy:
    Verwijder een applicatie met de bijhorende autorisaties.

    Na het verwijderen wordt een notificatie verstuurd.
    """
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
