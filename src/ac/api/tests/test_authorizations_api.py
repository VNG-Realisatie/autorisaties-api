from rest_framework import status
from rest_framework.test import APITestCase
from vng_api_common.constants import VertrouwelijkheidsAanduiding
from vng_api_common.tests import (
    JWTScopesMixin, get_operation_url, get_validation_errors
)

from ac.datamodel.tests.factories import ApplicatieFactory


class SetAuthorizationsTests(JWTScopesMixin, APITestCase):

    def test_create_application_with_all_permissions(self):
        """
        Test registration of an application with all authorizations.

        All authorizations should be granted because of the flag provided. This
        gives an option to do coarse-grained authorization for an application.

        TODO: add assertions on the underlying model instances.
        """
        url = get_operation_url('applicatie_create')

        data = {
            'client_ids': ['id1', 'id2'],
            'label': 'Melding Openbare Ruimte consumer',
            'heeftAlleAutorisatie': True,
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_application_with_detail_permissions(self):
        """
        Test registration of an application with limited authorizations.

        Fine-grained authorization can be achieved per ZaakType, which limits
        which scopes are allowed for this particular type. The same applies
        for maxVetrouwelijkheidaanduiding.

        TODO: add assertions on the underlying model instances.
        """
        url = get_operation_url('applicatie_create')

        data = {
            'client_ids': ['id1', 'id2'],
            'label': 'Melding Openbare Ruimte consumer',
            'autorisaties': [{
                'component': 'ZRC',
                'scopes': [
                    'zds.scopes.zaken.lezen',
                    'zds.scopes.zaken.aanmaken',
                ],
                'zaaktype': 'https://ref.tst.vng.cloud/zrc/api/v1/catalogus/1/zaaktypen/1',
                'maxVetrouwelijkheidaanduiding': VertrouwelijkheidsAanduiding.beperkt_openbaar,
            }, {
                'component': 'ZRC',
                'scopes': [
                    'zds.scopes.zaken.lezen',
                    'zds.scopes.zaken.aanmaken',
                    'zds.scopes.zaken.verwijderen',
                ],
                'zaaktype': 'https://ref.tst.vng.cloud/zrc/api/v1/catalogus/2/zaaktypen/1',
                'maxVetrouwelijkheidaanduiding': VertrouwelijkheidsAanduiding.zeer_geheim,
            }],
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_all_permissions_and_explicitly_provided(self):
        """
        Assert that you either specify heeftAlleAutorisatie or autorisaties.

        Part one of the XOR test.
        """
        url = get_operation_url('applicatie_create')

        data = {
            'client_ids': ['id1', 'id2'],
            'label': 'Melding Openbare Ruimte consumer',
            'heeftAlleAutorisatie': True,
            'autorisaties': [{
                'component': 'ZRC',
                'scopes': [
                    'zds.scopes.zaken.lezen',
                    'zds.scopes.zaken.aanmaken',
                ],
                'zaaktype': 'https://ref.tst.vng.cloud/zrc/api/v1/catalogus/1/zaaktypen/1',
                'maxVetrouwelijkheidaanduiding': VertrouwelijkheidsAanduiding.beperkt_openbaar,
            }],
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        error = get_validation_errors(response, 'nonFieldErrors')
        self.assertEqual(error['code'], 'ambiguous-authorizations-specified')

    def test_create_no_permissions_provided(self):
        """
        Assert that you either specify heeftAlleAutorisatie or autorisaties.

        Part two of the XOR test.
        """
        url = get_operation_url('applicatie_create')

        data = {
            'client_ids': ['id1', 'id2'],
            'label': 'Melding Openbare Ruimte consumer',
            'autorisaties': [],
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        error = get_validation_errors(response, 'nonFieldErrors')
        self.assertEqual(error['code'], 'missing-authorizations')

    def test_create_no_permissions_provided_2(self):
        """
        Assert that you either specify heeftAlleAutorisatie or autorisaties.

        Part three of the XOR test.
        """
        url = get_operation_url('applicatie_create')

        data = {
            'client_ids': ['id1', 'id2'],
            'label': 'Melding Openbare Ruimte consumer',
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        error = get_validation_errors(response, 'nonFieldErrors')
        self.assertEqual(error['code'], 'missing-authorizations')


class ReadAuthorizationsTests(JWTScopesMixin, APITestCase):

    @classmethod
    def setUpTestData(cls):
        ApplicatieFactory.create(
            client_ids=['id1', 'id2'],
            autorisaties__zaaktype='https://example.com',
            autorisaties__scopes=['dummy.scope'],
            autorisaties__max_vetrouwelijkheidaanduiding=VertrouwelijkheidsAanduiding.openbaar,
        )

    def test_filter_client_id_hit(self):
        url = get_operation_url('applicatie_list')

        response = self.client.get(url, {'client_id': 'id2'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)

    def test_filter_client_id_miss(self):
        url = get_operation_url('applicatie_list')

        response = self.client.get(url, {'client_id': 'id3'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 0)


class UpdateAuthorizationsTests(JWTScopesMixin, APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.applicatie = ApplicatieFactory.create(
            client_ids=['id1', 'id2'],
            autorisaties__zaaktype='https://example.com',
            autorisaties__scopes=['dummy.scope'],
            autorisaties__max_vetrouwelijkheidaanduiding=VertrouwelijkheidsAanduiding.openbaar,
        )

    def test_update_client_ids(self):
        url = get_operation_url('applicatie_partial_update', uuid=self.applicatie.uuid)

        response = self.client.patch(url, {'client_ids': ['id1']})

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_replace_authorizations(self):
        url = get_operation_url('applicatie_partial_update', uuid=self.applicatie.uuid)
        data = {
            'autorisaties': [{
                'component': 'ZRC',
                'scopes': [
                    'zds.scopes.zaken.lezen',
                    'zds.scopes.zaken.aanmaken',
                ],
                'maxVetrouwelijkheidaanduiding': VertrouwelijkheidsAanduiding.beperkt_openbaar,
                'zaaktype': 'https://ref.tst.vng.cloud/zrc/api/v1/catalogus/1/zaaktypen/1',
            }, {
                'component': 'ZRC',
                'scopes': [
                    'zds.scopes.zaken.lezen',
                    'zds.scopes.zaken.aanmaken',
                    'zds.scopes.zaken.verwijderen',
                ],
                'zaaktype': 'https://ref.tst.vng.cloud/zrc/api/v1/catalogus/2/zaaktypen/1',
                'maxVetrouwelijkheidaanduiding': VertrouwelijkheidsAanduiding.zeer_geheim,
            }],
        }

        response = self.client.patch(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
