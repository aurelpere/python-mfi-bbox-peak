FROM python:slim-buster

ENV PYTHONUNBUFFERED 1

RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential netcat \
  # psycopg2 and gdal/geos dependencies
  && apt-get install -y libpq-dev libproj-dev libgeos-dev libgdal-dev libgeos-dev\
  # Translations dependencies
  && apt-get install -y gettext \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

RUN addgroup --system django \
    && adduser --system --ingroup django django
ENV TZ="Europe/Paris"
# Requirements are installed here to ensure they will be cached.
COPY ./Dockerfiles/django/requirements.txt /requirements.txt
RUN pip install -r /requirements.txt


COPY ./Dockerfiles/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start
RUN chown django /start

WORKDIR /app

# copy project code
COPY . .

RUN chown -R django:django /app



USER django
#ENTRYPOINT ["/entrypoint"]
