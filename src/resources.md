# Resources

Dit document beschrijft de (RGBZ-)objecttypen die als resources ontsloten
worden met de beschikbare attributen.


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
