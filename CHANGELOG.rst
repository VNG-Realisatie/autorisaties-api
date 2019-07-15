===========
Wijzigingen
===========

0.4.0 (2019-07-15)
==================

Improvements towards release candidate

* Fixed some documentation
* Bumped to latest Django & vng-api-common releases
* Set up CI/CD to publish/deploy ``develop`` builds
* Added migration to new domains
* Enforced the uniqueness of ``Applicatie.clientIds`` entries
* Added API endpoint to fetch the application for a given Client ID

0.3.1 (2019-07-01)
==================

Fixed bug in docker start script preventing fixtures from being loaded.

0.3.0 (2019-06-19)
==================

Small feature release without breaking changes

* Bumped dependencies to (latest) security releases
* Translated API documentation
* Added fixture loading to container start script

0.2.5 (2019-06-03)
==================

Debugging

Also contains the 0.2.3 and 0.2.4 changes

* Enabled notification webhooks registration
* Fixed the AC notification handler
* Enabled the view-config page to debug component configuration

0.2.2 (2019-05-22)
==================

Update to latest versions of dependencies

0.2.0 (2019-05-20)
==================

Improved API docs

* updated to latest vng-api-common


0.1.0 (2019-04-05)
==================

* Initial release.
