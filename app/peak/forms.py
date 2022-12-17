from django import forms
from django.core.validators import RegexValidator


class BboxCoordinatesForm(forms.Form):
    minlatitude = forms.CharField(
        validators=[RegexValidator(regex=r"\d{1,3}\.\d{6}")])
    maxlatitude = forms.CharField(
        validators=[RegexValidator(regex=r"\d{1,3}\.\d{6}")])
    minlongitude = forms.CharField(
        validators=[RegexValidator(regex=r"\d{1,3}\.\d{6}")])
    maxlongitude = forms.CharField(
        validators=[RegexValidator(regex=r"\d{1,3}\.\d{6}")])


class WGS84CoordinatesForm(forms.Form):
    name = forms.CharField()
    altitude = forms.CharField(
        validators=[RegexValidator(regex=r"\d{1,4}[\.]?[\d{1,6}]?")])
    latitude = forms.CharField(
        validators=[RegexValidator(regex=r"\d{1,3}\.\d{6}")])
    longitude = forms.CharField(
        validators=[RegexValidator(regex=r"\d{1,3}\.\d{6}")])
    #point=geoforms.PointField(widget=geoforms.OSMWidget(
    #                        attrs={'map_width': 800,
    #                               'map_srid': 4326,
    #                               'map_height': 500,
    #                               'default_lat': 49.246292,
    #                               'default_lon':-123.116226,
    #                               'default_zoom': 7,}))
    #class Meta:
    #model = Peak
    #fields='__all__'


#    def clean(self):
#        cleaned_data = super().clean()
#        latitude = cleaned_data.get('latitude')
#        longitude = cleaned_data.get('longitude')
