from django.contrib.gis.db import models
from django.core.validators import RegexValidator


# Create your models here.
class Peak(models.Model):
    name = models.CharField(max_length=255)
    altitude = models.FloatField()
    latitude = models.FloatField(
        validators=[RegexValidator(regex=r"\d{1,3}\.\d{1,6}")])
    longitude = models.FloatField(
        validators=[RegexValidator(regex=r"\d{1,3}\.\d{1,6}")])
    point = models.PointField()

    class Meta:
        db_table = "peak_table"
