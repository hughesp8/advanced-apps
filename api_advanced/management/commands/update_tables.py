from django.core.management.base import BaseCommand, CommandError
from api_advanced.models import LuasStop
import luas.api
import json

class Command(BaseCommand):
    help = 'Updates the luas stop table'

    def handle(self, *args, **options):
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

