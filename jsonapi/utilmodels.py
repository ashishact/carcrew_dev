from django.db import models


class LatLon(models.Model):
    Latitude = models.DecimalField(max_digits=8, decimal_places=3)
    Longitude = models.DecimalField(max_digits=8, decimal_places=3)

    def __str__(self):
        return str(self.Latitude) + " , " + str(self.Longitude)
