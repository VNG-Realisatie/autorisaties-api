from django_filters.rest_framework import filters
from vng_api_common.authorizations.models import Applicatie
from vng_api_common.filtersets import FilterSet


class CharArrayFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class ApplicatieFilter(FilterSet):
    client_ids = CharArrayFilter(field_name='client_ids', lookup_expr='contains')

    class Meta:
        model = Applicatie
        fields = ('client_ids', )
