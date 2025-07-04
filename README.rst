===========================  ===============
Eigenaar                     Ingevuld door
===========================  ===============
Kennis centrum Architectuur  Rutger ter Borg
===========================  ===============

================
Autorisaties API
================

:Version: 1.0.1-alpha1
:Source: https://github.com/VNG-Realisatie/gemma-autorisatiecomponent
:Keywords: autorisatie, autz, zaakgericht werken, GEMMA

Introductie
===========

Diverse registraties beschermen hun resources tegen ongeautoriseerde toegang
op basis van scopes, zaaktype en vertrouwelijkheidaanduiding. Consumers
benaderen hierbij providers, en de providers dienen autorisatie-checks toe te
passen.

Deze component laat organisaties (lees: gemeentes) toe om per (taak)applicatie
te configureren welke autorisaties van toepassing zijn, gedetailleerd tot op
het niveau van zaaktype.

API specificaties
=================

|lint-oas| |generate-sdks| |generate-postman-collection|

==========  ==============  ====================================================================================================================================================================================================  =======================================================================================================================  =================================================================================================================================
Versie      Release datum   API specificatie                                                                                                                                                                                      Autorisaties                                                                                                             Notificaties
==========  ==============  ====================================================================================================================================================================================================  =======================================================================================================================  =================================================================================================================================
master       n.v.t.         `ReDoc <https://redocly.github.io/redoc/?url=https://raw.githubusercontent.com/VNG-Realisatie/gemma-autorisatiecomponent/master/src/openapi.yaml>`_,                                                  `Scopes <https://github.com/VNG-Realisatie/gemma-autorisatiecomponent/blob/master/src/autorisaties.md>`_                 `Berichtkenmerken <https://github.com/VNG-Realisatie/gemma-autorisatiecomponent/blob/master/src/notificaties.md>`_
                            `Swagger <https://petstore.swagger.io/?url=https://raw.githubusercontent.com/VNG-Realisatie/gemma-autorisatiecomponent/master/src/openapi.yaml>`_
                            (`verschillen <https://github.com/VNG-Realisatie/gemma-autorisatiecomponent/compare/1.0.0..master?diff=split#diff-b9c28fec6c3f3fa5cff870d24601d6ab7027520f3b084cc767aefd258cb8c40a>`_)
1.0.0       2019-11-18      `ReDoc <https://redocly.github.io/redoc/?url=https://raw.githubusercontent.com/VNG-Realisatie/gemma-autorisatiecomponent/1.0.0/src/openapi.yaml>`_,                                                   `Scopes <https://github.com/VNG-Realisatie/gemma-autorisatiecomponent/blob/1.0.0/src/autorisaties.md>`_                  `Berichtkenmerken <https://github.com/VNG-Realisatie/gemma-autorisatiecomponent/blob/1.0.0/src/notificaties.md>`_
                            `Swagger <https://petstore.swagger.io/?url=https://raw.githubusercontent.com/VNG-Realisatie/gemma-autorisatiecomponent/1.0.0/src/openapi.yaml>`_
==========  ==============  ====================================================================================================================================================================================================  =======================================================================================================================  =================================================================================================================================

Zie ook: `Alle versies en wijzigingen <https://github.com/VNG-Realisatie/gemma-autorisatiecomponent/blob/master/CHANGELOG.rst>`_

Ondersteuning
-------------

==========  ==============  ==========================  =================
Versie      Release datum   Einddatum ondersteuning     Documentatie
==========  ==============  ==========================  =================
1.x         2019-11-18      (nog niet bekend)           `Documentatie <https://vng-realisatie.github.io/gemma-zaken/standaard/autorisaties/index>`_
==========  ==============  ==========================  =================

Referentie implementatie
========================

|build-status| |coverage| |docker| |black| |python-versions|

Referentieimplementatie van de Autorisaties API. Ook wel
Autorisatiecomponent (AC) genoemd.

Ontwikkeld door `Maykin Media B.V. <https://www.maykinmedia.nl>`_ in opdracht
van VNG Realisatie.

Deze referentieimplementatie toont aan dat de API specificatie voor de
Autorisaties API implementeerbaar is, en vormt een voorbeeld voor andere
implementaties indien ergens twijfel bestaat.

Deze component heeft ook een `demo omgeving`_ waar leveranciers tegenaan kunnen
testen.

Links
=====

* Deze API is onderdeel van de `VNG standaard "API's voor Zaakgericht werken" <https://github.com/VNG-Realisatie/gemma-zaken>`_.
* Lees de `functionele specificatie <https://vng-realisatie.github.io/gemma-zaken/standaard/autorisaties/index>`_ bij de API specificatie.
* Bekijk de `demo omgeving`_ met de laatst gepubliceerde versie.
* Bekijk de `test omgeving <https://autorisaties-api.test.vng.cloud/>`_ met de laatste ontwikkel versie.
* Rapporteer `issues <https://github.com/VNG-Realisatie/gemma-zaken/issues>`_ bij vragen, fouten of wensen.
* Bekijk de `code <https://github.com/VNG-Realisatie/gemma-autorisatiecomponent/>`_ van de referentie implementatie.

.. _`demo omgeving`: https://autorisaties-api.vng.cloud/

Licentie
========

Copyright © VNG Realisatie 2018 - 2020

Licensed under the EUPL_

.. _EUPL: LICENCE.md

.. |build-status| image:: https://github.com/VNG-Realisatie/autorisaties-api/workflows/ci-build/badge.svg
    :alt: Build status
    :target: https://github.com/VNG-Realisatie/autorisaties-api/actions?query=workflow%3Aci-build

.. |requirements| image:: https://requires.io/github/VNG-Realisatie/gemma-autorisatiecomponent/requirements.svg?branch=master
     :alt: Requirements status

.. |coverage| image:: https://codecov.io/github/VNG-Realisatie/gemma-autorisatiecomponent/branch/master/graphs/badge.svg?branch=master
    :alt: Coverage
    :target: https://codecov.io/gh/VNG-Realisatie/gemma-autorisatiecomponent

.. |docker| image:: https://img.shields.io/badge/docker-latest-blue.svg
    :alt: Docker image
    :target: https://hub.docker.com/r/vngr/autorisaties-api

.. |black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :alt: Code style
    :target: https://github.com/psf/black

.. |python-versions| image:: https://img.shields.io/badge/python-3.6%2B-blue.svg
    :alt: Supported Python version

.. |lint-oas| image:: https://github.com/VNG-Realisatie/gemma-autorisatiecomponent/workflows/lint-oas/badge.svg
    :alt: Lint OAS
    :target: https://github.com/VNG-Realisatie/gemma-autorisatiecomponent/actions?query=workflow%3Alint-oas

.. |generate-sdks| image:: https://github.com/VNG-Realisatie/gemma-autorisatiecomponent/workflows/generate-sdks/badge.svg
    :alt: Generate SDKs
    :target: https://github.com/VNG-Realisatie/gemma-autorisatiecomponent/actions?query=workflow%3Agenerate-sdks

.. |generate-postman-collection| image:: https://github.com/VNG-Realisatie/gemma-autorisatiecomponent/workflows/generate-postman-collection/badge.svg
    :alt: Generate Postman collection
    :target: https://github.com/VNG-Realisatie/gemma-autorisatiecomponent/actions?query=workflow%3Agenerate-postman-collection
