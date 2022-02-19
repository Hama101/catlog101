import django_filters as df

from .models import *

class Filters(df.FilterSet):
    class Meta:
        model = Games
        fields = '__all__'