from rest_framework import serializers

from .models import LuasStop

class LuasStopSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LuasStop
        fields = ('short_name','long_name','line','latitude','longitude','status','trams')
