from vng_api_common.conf.api import *  # noqa - imports white-listed

REST_FRAMEWORK = BASE_REST_FRAMEWORK.copy()
REST_FRAMEWORK['DEFAULT_PAGINATION_CLASS'] = 'rest_framework.pagination.PageNumberPagination'
REST_FRAMEWORK['PAGE_SIZE'] = 100

SECURITY_DEFINITION_NAME = 'JWT-Claims'

SWAGGER_SETTINGS = BASE_SWAGGER_SETTINGS.copy()

_default_field_inspectors = list(BASE_SWAGGER_SETTINGS['DEFAULT_FIELD_INSPECTORS'])
_default_field_inspectors.remove('vng_api_common.inspectors.geojson.GeometryFieldInspector')

SWAGGER_SETTINGS.update({
    'DEFAULT_INFO': 'ac.api.schema.info',

    'SECURITY_DEFINITIONS': {
        SECURITY_DEFINITION_NAME: {
            # OAS 3.0
            'type': 'http',
            'scheme': 'bearer',
            'bearerFormat': 'JWT',
            # not official...
            # 'scopes': {},  # TODO: set up registry that's filled in later...

            # Swagger 2.0
            # 'name': 'Authorization',
            # 'in': 'header'
            # 'type': 'apiKey',
        }
    },

    'DEFAULT_FIELD_INSPECTORS': tuple(_default_field_inspectors),
})

GEMMA_URL_INFORMATIEMODEL_VERSIE = '1.0'
