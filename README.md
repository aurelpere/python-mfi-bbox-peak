[![Test-Lint-Format](https://github.com/aurelpere/python-mfi-bbox-peak/actions/workflows/main.yml/badge.svg)](https://github.com/aurelpere/python-mfi-bbox-peak/actions/workflows/main.yml)

# utilisation 
<br>

`git clone https://github.com/aurelpere/python-mfi-bbox-peak.git`
>telecharger le depot
<br>

<br>

`cd python-mfi-bbox-peak && docker-compose up`
>déployer le serveur django (docker et docker-compose doivent être installés sur votre ordinateur)
<br>

<br>

`localhost:8000`
>Entrer cette adresse dans votre navigateur internet pour accéder à l'interface du  pour ajouter des points, les éditer, les supprimer et définir une bounding box
<br>
<br>

<br>

`localhost:8000/peak`
>le endpoint  pour consulter la liste des peaks (GET) ou en ajouter (POST) par l'interface de django-rest-framework-gis
<br>

>note: pour ajouter un peak, bien penser à définir le champ "point" avec la syntaxe `SRID=4326;POINT (<longitude> <latitude>)` ou avec la syntaxe `{"type": "Point", "coordinates": [<longitude>, <latitude>]}` en remplacant <longitude> par la longitude (wgs84) et <latitude> par la latitude (wgs84) avec 6 décimales
<br>

<br>

`localhost:8000/peaks/?in_bbox=<min lon>,<min lat>,<max lon>,<max lat>`
>le endpoint  pour consulter la liste des peaks (GET) avec une bounding box (min Lon, min Lat, max Lon, max Lat), le endpoint
<br>

<br>

`make test`
>pour lancer les tests (1 test de création d'un enregistrement dans la bdd 5 tests CRUD sur le endpoint /peak). Ils sont automatiquement lancés au déploiement du code sur le dépot github (voir les fichiers dans le sous-répertoire tests). Attention à bien supprimer les container et volumes docker précédemment crées.
<br>

