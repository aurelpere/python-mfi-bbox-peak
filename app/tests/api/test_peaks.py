import pytest
from peak import models
from geojson import Point
from django.contrib.gis.geos import Point as GeosPoint
from peak.models import Peak
import requests
@pytest.mark.django_db
def test_peak_create():
    p = Peak(name='test',
                    altitude=4809,
                    longitude=6.865175,
                    latitude=45.832622,
                    point="SRID=4326;POINT (6.865175 45.832622)")
    p.save()
    p=Peak.objects.all().first() # pylint: disable=E1101
    assert p.altitude == float("4809")
    assert p.longitude == float("6.865175")
    assert p.latitude == float("45.832622")
    assert p.point.coords==GeosPoint(
        (float(6.865175), float(45.832622))).coords

@pytest.mark.django_db
def post_peak_1():
    p = models.Peak(name='test',
                    altitude=4809,
                    longitude=6.865175,
                    latitude=45.832622,
                    point="SRID=4326;POINT (6.865175 45.832622)")
    p.save()


@pytest.mark.django_db
def post_peak_2():
    p = models.Peak(name='test2',
                    altitude=3299,
                    longitude=-0.147713,
                    latitude=42.773837,
                    point="SRID=4326;POINT (-0.147713 42.773837)")
    p.save()


@pytest.mark.django_db
def post_peak_3():
    p = models.Peak(name='test3',
                    altitude=0,
                    longitude=1.234567,
                    latitude=3.456789,
                    point="SRID=4326;POINT (1.234567 3.456789)")
    p.save()


@pytest.mark.django_db
def test_create_peak(client):
    payload = dict(name="test",
                   altitude=4809,
                   longitude=6.865175,
                   latitude=45.832622,
                   point="SRID=4326;POINT (6.865175 45.832622)")
    response = client.post(path='/peak/', data=payload)
    assert response.status_code == 201
    data = models.Peak.objects.all().first()  # pylint: disable=E1101
    assert data.name == payload["name"]
    assert data.altitude == float(payload["altitude"])
    assert data.longitude == float(payload["longitude"])
    assert data.latitude == float(payload["latitude"])
    assert data.point == payload["point"]


@pytest.mark.django_db
def test_read_peak(client):
    post_peak_1()
    post_peak_2()
    response = client.get(path='/peak/')
    assert response.data[0]["name"] == "test"
    assert response.data[0]["altitude"] == float(4809)
    assert response.data[0]["longitude"] == float(6.865175)
    assert response.data[0]["latitude"] == float(45.832622)
    assert response.data[0]["point"] == Point(
        (float(6.865175), float(45.832622)))
    assert response.data[1]["name"] == "test2"
    assert response.data[1]["altitude"] == float(3299)
    assert response.data[1]["longitude"] == float(-0.147713)
    assert response.data[1]["latitude"] == float(42.773837)
    assert response.data[1]["point"] == Point(
        (float(-0.147713), float(42.773837)))


@pytest.mark.django_db
def test_update_peak(client):
    post_peak_1()
    uuid = models.Peak.objects.filter(name='test').values()[0]["id"]  # pylint: disable=E1101
    print(uuid)
    payload = dict(name="test2",
                   altitude=3299,
                   longitude=-0.147713,
                   latitude=42.773837,
                   point="SRID=4326;POINT (-0.147713 42.773837)")
    client.put(path=f'/peak/{uuid}/', data=payload)
    response = client.get(path=f'/peak/{uuid}/')
    print(response.data)
    assert response.data["name"] == payload["name"]
    assert response.data["altitude"] == float(payload["altitude"])
    assert response.data["longitude"] == float(payload["longitude"])
    assert response.data["latitude"] == float(payload["latitude"])
    assert response.data["point"] == Point(
        (float(payload["longitude"]), float(payload["latitude"])))


@pytest.mark.django_db
def test_delete_peak(client):
    post_peak_1()
    uuid = models.Peak.objects.filter(name='test').values()[0]["id"]  # pylint: disable=E1101
    client.delete(path=f'/peak/{uuid}/')
    data = models.Peak.objects.all().first()  # pylint: disable=E1101
    assert data is None


@pytest.mark.django_db
def test_bbox_request(client):
    post_peak_1()
    post_peak_2()
    post_peak_3()
    response = client.get(
        path=f'/peak/?in_bbox={6.000000},{45.000000},{7.000000},{46.000000}')
    print(response.data)
    assert response.data[0]["name"] == "test"
    assert response.data[0]["altitude"] == float(4809)
    assert response.data[0]["longitude"] == float(6.865175)
    assert response.data[0]["latitude"] == float(45.832622)
    assert response.data[0]["point"] == Point(
        (float(6.865175), float(45.832622)))
    response = client.get(
        path=f'/peak/?in_bbox={-1},{42.000000},{7.000000},{46.000000}')
    print(response.data)
    assert response.data[0]["name"] == "test"
    assert response.data[0]["altitude"] == float(4809)
    assert response.data[0]["longitude"] == float(6.865175)
    assert response.data[0]["latitude"] == float(45.832622)
    assert response.data[0]["point"] == Point(
        (float(6.865175), float(45.832622)))
    assert response.data[1]["name"] == "test2"
    assert response.data[1]["altitude"] == float(3299)
    assert response.data[1]["longitude"] == float(-0.147713)
    assert response.data[1]["latitude"] == float(42.773837)
    assert response.data[1]["point"] == Point(
        (float(-0.147713), float(42.773837)))
    response = client.get(
        path=f'/peak/?in_bbox={-1},{2.000000},{7.000000},{46.000000}')
    print(response.data)
    assert response.data[0]["name"] == "test"
    assert response.data[0]["altitude"] == float(4809)
    assert response.data[0]["longitude"] == float(6.865175)
    assert response.data[0]["latitude"] == float(45.832622)
    assert response.data[0]["point"] == Point(
        (float(6.865175), float(45.832622)))
    assert response.data[1]["name"] == "test2"
    assert response.data[1]["altitude"] == float(3299)
    assert response.data[1]["longitude"] == float(-0.147713)
    assert response.data[1]["latitude"] == float(42.773837)
    assert response.data[1]["point"] == Point(
        (float(-0.147713), float(42.773837)))
    assert response.data[2]["name"] == "test3"
    assert response.data[2]["altitude"] == float(0)
    assert response.data[2]["longitude"] == float(1.234567)
    assert response.data[2]["latitude"] == float(3.456789)
    assert response.data[2]["point"] == Point(
        (float(1.234567), float(3.456789)))
