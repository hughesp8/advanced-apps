from django.db import models

class LuasStop(models.Model):
    short_name = models.CharField(primary_key=True, max_length=255, null=False, blank=False)
    long_name = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    line = models.CharField(max_length=20, null=True, blank=True)
    trams = models.CharField(max_length=950, null=True, blank=True)


    def __str__(self):
        return "{} - {}".format(self.long_name, self.status)
