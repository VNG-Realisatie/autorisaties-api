from django.conf import settings

from drf_yasg import openapi
from vng_api_common.notifications.utils import notification_documentation

from .kanalen import KANAAL_AUTORISATIES

description = f"""Een API om een autorisatiecomponent (AC) te benaderen.

De `AUTORISATIE` is het kernobject in deze API. Autorisaties worden toegekend
aan applicaties. Een applicatie is een representatie van een (web) app die
communiceert met de API van (andere) componenten, zoals het ZRC, DRC, ZTC en
BRC.

Deze API laat toe om autorisaties van een (taak)applicatie te beheren en uit
te lezen.

**Afhankelijkheden**

Deze API is afhankelijk van:

* Notificaties API

**Autorisatie**

Deze API vereist autorisatie. Je kan de
[token-tool](https://zaken-auth.vng.cloud/) gebruiken om JWT-tokens te
genereren.

### Notificaties

{notification_documentation(KANAAL_AUTORISATIES)}

**Handige links**

* [Documentatie](https://zaakgerichtwerken.vng.cloud/standaard)
* [Zaakgericht werken](https://zaakgerichtwerken.vng.cloud)
"""

info = openapi.Info(
    title=f"{settings.PROJECT_NAME} API",
    default_version=settings.API_VERSION,
    description=description,
    contact=openapi.Contact(
        email="standaarden.ondersteuning@vng.nl",
        url="https://zaakgerichtwerken.vng.cloud"
    ),
    license=openapi.License(
        name="EUPL 1.2",
        url='https://opensource.org/licenses/EUPL-1.2'
    ),
)
