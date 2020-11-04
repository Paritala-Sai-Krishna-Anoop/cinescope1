import django_filters
from .models import *

class audiofilter(django_filters.FilterSet):
     class Meta:
         model = audio
         fields = ['type']


class videoefilter(django_filters.FilterSet):
    class Meta:
        model = videoe
        fields = ['softwaretype']



class jobfilter(django_filters.FilterSet):
    class Meta:
        model = mainman
        fields = ['area_of_expertees']