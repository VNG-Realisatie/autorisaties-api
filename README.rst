====================
Autorisatiecomponent
====================

:Version: 1.0.0
:Source: https://github.com/VNG-Realisatie/gemma-autorisatiecomponent
:Keywords: autorisatie, autz, zaakgericht werken, GEMMA
:PythonVersion: 3.7

|build-status| |black| |lint-oas| |generate-sdks| |generate-postman-collection|

Referentieimplementatie van de autorisatiecomponent (AC).

Inleiding
=========

Diverse registraties beschermen hun resources tegen ongeautoriseerde toegang
op basis van scopes, zaaktype en vertrouwelijkheidaanduiding. Consumers
benaderen hierbij providers, en de providers dienen autorisatie-checks toe te
passen.

Deze component laat organisaties (lees: gemeentes) toe om per (taak)applicatie
te configureren welke autorisaties van toepassing zijn, gedetailleerd tot op
het niveau van zaaktype.

Deze component heeft ook een `testomgeving`_ waar leveranciers tegenaan kunnen
testen.

Documentatie
============

Zie ``INSTALL.rst`` voor installatieinstructies, beschikbare instellingen en
commando's.

Indien je actief gaat ontwikkelen aan deze component raden we aan om niet van
Docker gebruik te maken. Indien je deze component als black-box wil gebruiken,
raden we aan om net wel van Docker gebruik te maken.

Referenties
===========

* `Issues <https://github.com/VNG-Realisatie/gemma-autorisatiecomponent/issues>`_
* `Code <https://github.com/VNG-Realisatie/gemma-autorisatiecomponent>`_


.. |build-status| image:: https://travis-ci.org/VNG-Realisatie/gemma-autorisatiecomponent.svg?branch=master
    :alt: Build status
    :target: https://travis-ci.org/VNG-Realisatie/gemma-autorisatiecomponent

.. |requirements| image:: https://requires.io/github/VNG-Realisatie/gemma-autorisatiecomponent/requirements.svg?branch=master
     :target: https://requires.io/github/VNG-Realisatie/gemma-autorisatiecomponent/requirements/?branch=master
     :alt: Requirements status

.. |black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black

.. |lint-oas| image:: https://github.com/VNG-Realisatie/gemma-autorisatiecomponent/workflows/lint-oas/badge.svg
    :alt: Lint OAS
    :target: https://github.com/VNG-Realisatie/gemma-autorisatiecomponent/actions?query=workflow%3Alint-oas

.. |generate-sdks| image:: https://github.com/VNG-Realisatie/gemma-autorisatiecomponent/workflows/generate-sdks/badge.svg
    :alt: Generate SDKs
    :target: https://github.com/VNG-Realisatie/gemma-autorisatiecomponent/actions?query=workflow%3Agenerate-sdks

.. |generate-postman-collection| image:: https://github.com/VNG-Realisatie/gemma-autorisatiecomponent/workflows/generate-postman-collection/badge.svg
    :alt: Generate Postman collection
    :target: https://github.com/VNG-Realisatie/gemma-autorisatiecomponent/actions?query=workflow%3Agenerate-postman-collection

.. _testomgeving: https://autorisaties-api.vng.cloud/

Licentie
========

Copyright © VNG Realisatie 2019

Licensed under the EUPL_

.. _EUPL: LICENCE.md
