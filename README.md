# utilisation 
>telecharger le depot
`git clone https://github.com/aurelpere/python-mfi-bbox-peak.git`

>déployer le serveur django (docker et docker-compose doivent être installés sur votre ordinateur)
`cd python-mfi-bbox-peak && docker-compose up`

>pour consulter le site internet produit (frontend), aller dans un navigateur et entrer 
`localhost:8000`

>pour consulter la liste des peaks (GET) ou en ajouter (POST) par l'interface de django-rest-framework-gis, le endpoint est le suivant:
`localhost:8000/peak`

>note: pour ajouter un peak, bien penser à définir le champ "point" avec la syntaxe `SRID=4326;POINT (<longitude> <latitude>)` ou avec la syntaxe `{"type": "Point", "coordinates": [<longitude>, <latitude>]}` en remplacant <longitude> par la longitude (wgs84) et <latitude> par la latitude (wgs84) avec 6 décimales

>pour consulter la liste des peaks (GET) avec une bounding box (min Lon, min Lat, max Lon, max Lat), le endpoint est le suivant:
`localhost:8000/peaks/?in_bbox=<min lon>,<min lat>,<max lon>,<max lat>`
exemple
`localhost:8000/peaks/?in_bbox=0,0,10,10`

>Le frontend donne une interface basique pour ajouter des points, les éditer, les supprimer et définir une bounding box
`localhost:8000`

>des tests ont été écrits (1 test de création d'un enregistrement dans la bdd 5 tests CRUD sur le endpoint /peak) et sont lancés au déploiement du code sur le dépot github (voir les fichiers dans le sous-répertoire tests). Pour lancer les tests localement, supprimer les container et volumes docker précédemment crées et lancer les tests avec la commande:
`make test`

