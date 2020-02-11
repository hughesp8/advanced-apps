from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets

from .serializers import LuasStopSerializer
from .models import LuasStop
import luas.api
import json

class LuasStopViewSet(viewsets.ModelViewSet):
    queryset = LuasStop.objects.all().order_by('short_name')
    serializer_class = LuasStopSerializer

def BackgroundDatabaseRefresh(request):
    if request.META.get('HTTP_X_APPENGINE_CRON'):
        luas_client = luas.api.LuasClient()
        for stop in LuasStop.objects.all():
            try:
                updated_stop = luas_client.stop_details(stop.short_name)
                stop.status = updated_stop['status']
                stop.trams = json.dumps(updated_stop['trams'])
                #make your API request here
                #suppose champ_image is what you retrieve from the API
                stop.save()
                print("Updated stop: {}".format(stop.long_name))
            except:
                print("Could not update stop: {}".format(stop.long_name))
        print("Stop updates complete!")
      # Request comes from GCP Cron, so do a bunch of stuff.
    else:
        return HttpResponse(status="403")
    return HttpResponse(status="200")

# Create your views here.
