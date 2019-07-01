====================
Autorisatiecomponent
====================

:Version: 0.3.1
:Source: https://github.com/VNG-Realisatie/gemma-autorisatiecomponent
:Keywords: autorisatie, autz, zaakgericht werken, GEMMA
:PythonVersion: 3.7

|build-status|

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


.. |build-status| image:: http://jenkins.nlx.io/buildStatus/icon?job=gemma-autorisatiecomponent-stable
    :alt: Build status
    :target: http://jenkins.nlx.io/job/gemma-autorisatiecomponent-stable

.. |requirements| image:: https://requires.io/github/VNG-Realisatie/gemma-autorisatiecomponent/requirements.svg?branch=master
     :target: https://requires.io/github/VNG-Realisatie/gemma-autorisatiecomponent/requirements/?branch=master
     :alt: Requirements status

.. _testomgeving: https://ref.tst.vng.cloud/AC/

Licentie
========

Copyright © VNG Realisatie 2019

Licensed under the EUPL_

.. _EUPL: LICENCE.md
