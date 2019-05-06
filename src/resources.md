# Resources

Dit document beschrijft de (RGBZ-)objecttypen die als resources ontsloten
worden met de beschikbare attributen.


## Autorisatie

Objecttype op [GEMMA Online](https://www.gemmaonline.nl/index.php/Rgbz_1.0/doc/objecttype/autorisatie)

| Attribuut | Omschrijving | Type | Verplicht | CRUD* |
| --- | --- | --- | --- | --- |
| component | Component waarop autorisatie van toepassing is.

De mapping van waarden naar weergave is als volgt:

* `AC` - Autorisatiecomponent
* `NRC` - Notificatierouteringcomponent
* `ZRC` - Zaakregistratiecomponent
* `ZTC` - Zaaktypecatalogus
* `DRC` - Documentregistratiecomponent
* `BRC` - Besluitregistratiecomponent | string | ja | C​R​U​D |
| componentWeergave |  | string | nee | ~~C~~​R​~~U~~​~~D~~ |
| scopes | Komma-gescheiden lijst van scope labels. | array | ja | C​R​U​D |
| zaaktype | URL naar het zaaktype waarop de autorisatie van toepassing is. | string | nee | C​R​U​D |
| maxVertrouwelijkheidaanduiding | Maximaal toegelaten vertrouwelijkheidaanduiding (inclusief). | string | nee | C​R​U​D |

## Applicatie

Objecttype op [GEMMA Online](https://www.gemmaonline.nl/index.php/Rgbz_1.0/doc/objecttype/applicatie)

| Attribuut | Omschrijving | Type | Verplicht | CRUD* |
| --- | --- | --- | --- | --- |
| url |  | string | nee | ~~C~~​R​~~U~~​~~D~~ |
| clientIds | Komma-gescheiden lijst van consumer identifiers (hun client_id). | array | ja | C​R​U​D |
| label | Een leesbare representatie van de applicatie, voor eindgebruikers. | string | ja | C​R​U​D |
| heeftAlleAutorisaties | Indien alle autorisaties gegeven zijn, dan hoeven deze niet individueel opgegeven te worden. Gebruik dit alleen als je de consumer helemaal vertrouwt. | boolean | nee | C​R​U​D |
| autorisaties |  | array | nee | C​R​U​D |


* Create, Read, Update, Delete
