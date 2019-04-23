import logging

from django.db import transaction
from rest_framework import serializers

from vng_api_common.authorizations.models import Autorisatie, Applicatie


logger = logging.getLogger(__name__)


class AutorisatieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Autorisatie
        fields = (
            'component',
            'zaaktype',
            'scopes',
            'maximale_vertrouwelijkheidaanduiding',
        )


class ApplicatieSerializer(serializers.HyperlinkedModelSerializer):
    autorisaties = AutorisatieSerializer(many=True)

    class Meta:
        model = Applicatie
        fields = (
            'url',
            'client_ids',
            'label',
            'autorisaties'
        )
        extra_kwargs = {
            'url': {
                'lookup_field': 'uuid',
            },
        }

    @transaction.atomic
    def create(self, validated_data):
        autorisaties_data = validated_data.pop('autorisaties')
        applicatie = super().create(validated_data)

        for auth in autorisaties_data:
            Autorisatie.objects.create(**auth, applicatie=applicatie)

        return applicatie

    @transaction.atomic
    def update(self, instance, validated_data):
        autorisaties_data = validated_data.pop('autorisaties')
        applicatie = super().update(instance, validated_data)

        # in case of update autorisaties - remove all related autorisaties
        if autorisaties_data:
            applicatie.autorisaties.all().delete()
            for auth in autorisaties_data:
                Autorisatie.objects.create(**auth, applicatie=applicatie)

        return applicatie
