
# utilisation 
<br>

`git clone https://github.com/aurelpere/python-mfi-bbox-peak.git`
>download repository
<br>

`cd python-mfi-bbox-peak && docker-compose up`
>deploy django server locally (docker and docker compose must be installed)
<br>

`localhost:8000`
>enter this adress in your browser to get the website (django frontend). you can retrieve the list of peaks, add some, edit and delete through an interface querying the /peak/ rest api endpoint
<br>

`localhost:8000/peak`
>CRUD endpoint (backend django). django-rest-framework-gis module provides a web interface on this adress if you enter it in your browser. fixtures have been added to django boot, so you should see vignemale and mont-blanc records in the list
<br>

>note: to add a peak, the "point" field must follow this syntax : `SRID=4326;POINT (<longitude> <latitude>)` or `{"type": "Point", "coordinates": [<longitude>, <latitude>]}`. <longitude> and <latitude> must be provided with 6 decimals in wgs84 coordinates
<br>

`localhost:8000/peak/?in_bbox=<min lon>,<min lat>,<max lon>,<max lat>`
>endpoint for getting peaks in the bounding box provided
<br>

`localhost:8000/peak/?in_bbox=6.0,45.0,7.0,46.0`
>if you enter this adress in your browser, you should get the records in the bounding box provided, which is mont-blanc record only
<br>

`make test`
>this command launches tests (1 test for save a record in the database 5 tests for CRUD on th /peak/ endpoint). See files in /tests subfolder for details. The tests are automatically launched when deploying code on github repository through github actions. The status badge in this readme at the top provides the results of the tests.
<br>

