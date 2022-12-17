from django.shortcuts import render, redirect
from peak.forms import WGS84CoordinatesForm
from peak.forms import BboxCoordinatesForm
from peak.models import Peak
#from django.contrib.gis.geos import Point
from rest_framework import viewsets
from peak.serializer import PeakSerializer
from rest_framework_gis.filters import InBBoxFilter
from django.urls import reverse
import requests


class PeakViewSet(viewsets.ModelViewSet):
    queryset = Peak.objects.all().order_by('name')  # pylint: disable=E1101
    serializer_class = PeakSerializer
    bbox_filter_field = 'point'
    filter_backends = (InBBoxFilter, )
    bbox_filter_include_overlapping = True  # Optional


def index(request):
    return render(request, 'index.html')


def bbox(request):
    if request.method == "POST":
        form = BboxCoordinatesForm(request.POST)
        if form.is_valid():
            print("form is valid")
            try:
                minlongitude = float(request.POST.get('minlongitude'))
                maxlongitude = float(request.POST.get('maxlongitude'))
                minlatitude = float(request.POST.get('minlatitude'))
                maxlatitude = float(request.POST.get('maxlatitude'))
                #for direct db query
                #peaks = Peak.objects.filter(longitude__lt=maxlongitude).filter(longitude__gt=minlongitude).filter(latitude__lt=maxlatitude).filter(latitude__gt=minlatitude)
                r = requests.get(
                    f'{request.build_absolute_uri(location=reverse("peak-list"))}?in_bbox={minlongitude},{minlatitude},{maxlongitude},{maxlatitude}',
                    timeout=10).json()
                print(r)
                return render(request, 'show.html', {'peaks': r})
            except Exception as e:  # pylint: disable=W0703
                print(e)
        else:
            print("form is not valid")
            print(form.errors.as_data())
    else:
        form = BboxCoordinatesForm()
    return render(request, 'bbox.html', {'form': form})


def create(request):
    if request.method == "POST":
        print(request.POST)
        form = WGS84CoordinatesForm(request.POST)
        if form.is_valid():
            print("form is valid")
            try:
                data = form.cleaned_data
                #attention, avec la requete post, il y a un cast de chaine vers float entre le formulaire et la valeur récupérée par python
                #et/ou entre la chaine transmise dans la requete post et la valeur enregistrée dans la bdd par python
                #la validateur à 6 décimales provoque un bug lorsque les derniers chiffres de la chaine sont 0 (le cast en float supprime les derniers zero)
                #c'est pour cette raison qu'on a définit un validateur à 1 à 6 décimales
                data[
                    "point"] = f"SRID=4326;POINT ({request.POST.get('longitude')} {request.POST.get('latitude')})"
                print("form data:")
                print(data)
                r = requests.post(
                    request.build_absolute_uri(location=reverse('peak-list')),
                    timeout=10,
                    data=data)
                print(r.text)
                return redirect('/show')
            except Exception as e:  # pylint: disable=W0703
                print(e)
        else:
            print("form is not valid")
            print(form.errors.as_data())
    else:
        form = WGS84CoordinatesForm()
    return render(request, 'create.html', {'form': form})


    # if request.method == "POST":
    #     form=WGS84CoordinatesForm(request.POST)
    #     if form.is_valid():
    #         try:
    #             name = request.POST.get('name')
    #             altitude= float(request.POST.get('altitude'))
    #             longitude = float(request.POST.get('longitude'))
    #             latitude = float(request.POST.get('latitude'))
    #             point = Point(longitude,latitude,srid=4326)
    #             #logger.info(type(point))
    #             insert = Peak(name=name,altitude=altitude,longitude=longitude,latitude=latitude,point=point)
    #             insert.save()
    #             return redirect('/show')
    #         except Exception as e:
    #             print(e)
    #             pass
    # else:
    #     form=WGS84CoordinatesForm()
    # return render(request,'create.html',{'form':form})
def show(request):
    #peaks = Peak.objects.all() for direct query on the db
    r = requests.get(request.build_absolute_uri(location=reverse('peak-list')),
                     timeout=10).json()
    print(r)
    print(type(r))
    return render(request, "show.html", {'peaks': r})


def edit(request, id):  # pylint: disable=W0622
    #peak = Peak.objects.get(id=id) for direct query on db
    if request.method == "POST":
        print(request.POST)
        form = WGS84CoordinatesForm(request.POST)
        if form.is_valid():
            print("form is valid")
            try:
                data = form.cleaned_data
                #peak.name = request.POST.get('name')
                #peak.altitude= float(request.POST.get('altitude'))
                #peak.longitude = float(request.POST.get('longitude'))
                #peak.latitude = float(request.POST.get('latitude'))
                #peak.point = Point(peak.longitude,peak.latitude,srid=4326)
                #peak.save()
                data[
                    "point"] = f"SRID=4326;POINT ({request.POST.get('longitude')} {request.POST.get('latitude')})"
                print("form data:")
                print(data)
                r = requests.put(
                    f'{request.build_absolute_uri(location=reverse("peak-list"))}{id}/',
                    timeout=10,
                    data=data)
                return redirect('/show')
            except Exception as e:  # pylint: disable=W0703
                print(e)
        else:
            print("form is not valid")
            print(form.errors.as_data())
    else:
        r = requests.get(
            f'{request.build_absolute_uri(location=reverse("peak-list"))}{id}/',
            timeout=10).json()
        form = WGS84CoordinatesForm(r)
    return render(request, 'edit.html', {'form': form, 'uuid': id})


def destroy(request, id):  # pylint: disable=W0622
    #peak = Peak.objects.get(id=id)
    #peak.delete()
    requests.delete(
        f'{request.build_absolute_uri(location=reverse("peak-list"))}{id}/',
        timeout=10)
    return redirect("/show")
