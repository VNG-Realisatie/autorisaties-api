# Resources

Dit document beschrijft de (RGBZ-)objecttypen die als resources ontsloten
worden met de beschikbare attributen.


## Autorisatie

Objecttype op [GEMMA Online](https://www.gemmaonline.nl/index.php/Rgbz_1.0/doc/objecttype/autorisatie)

| Attribuut | Omschrijving | Type | Verplicht | CRUD* |
| --- | --- | --- | --- | --- |
| component | Name of the component to authorize | string | ja | C​R​U​D |
| zaaktype | Url of the zaaktype that is allowed | string | ja | C​R​U​D |
| scopes | Comma-separated list of identifiers used for authentication | array | ja | C​R​U​D |
| maxVertrouwelijkheidaanduiding | Maximum level of confidentiality that is allowed | string | ja | C​R​U​D |

## Applicatie

Objecttype op [GEMMA Online](https://www.gemmaonline.nl/index.php/Rgbz_1.0/doc/objecttype/applicatie)

| Attribuut | Omschrijving | Type | Verplicht | CRUD* |
| --- | --- | --- | --- | --- |
| url |  | string | nee | ~~C~~​R​~~U~~​~~D~~ |
| clientIds | Comma-separated list of identifiers used for authentication | array | ja | C​R​U​D |
| label | A human readable representation of the application | string | ja | C​R​U​D |
| heeftAlleAutorisaties | Globally allows everything | boolean | nee | C​R​U​D |
| autorisaties |  | array | nee | C​R​U​D |


* Create, Read, Update, Delete
