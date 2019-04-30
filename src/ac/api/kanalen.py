from vng_api_common.notifications.kanalen import Kanaal

from vng_api_common.authorizations.models import Applicatie

KANAAL_AUTORISATIES = Kanaal(
    'autorisaties',
    main_resource=Applicatie,
    kenmerken=()
)
