import django_filters
from .models import *

class TempFilter(django_filters.FilterSet):
    class Meta:
        model = Valeurs
        fields = '__all__'
        exclude = ['datetime','time','temperature','humidite','pression','pnt_de_rosée','humidite_absolue','tension_de_vapeur','pression_cal']
        
class HumFilter(django_filters.FilterSet):
    class Meta:
        model = Valeurs
        fields = '__all__'
        exclude = ['datetime','time','humidite','temperature','pression','pnt_de_rosée','humidite_absolue','tension_de_vapeur','pression_cal']

class PresFilter(django_filters.FilterSet):
    class Meta:
        model = Valeurs
        fields = '__all__'
        exclude = ['datetime','time','pression','temperature','humidite','pnt_de_rosée','humidite_absolue','tension_de_vapeur','pression_cal']
        
class PointDRFilter(django_filters.FilterSet):
    class Meta:
        model = Valeurs
        fields = '__all__'
        exclude = ['datetime','time','temperature','pnt_de_rosée','pression','humidite','humidite_absolue','tension_de_vapeur','pression_cal']
        
class HumAbFilter(django_filters.FilterSet):
    class Meta:
        model = Valeurs
        fields = '__all__'
        exclude = ['datetime','time','humidite_absolue','temperature','pression','pnt_de_rosée','humidite','tension_de_vapeur','pression_cal']
        
class TensionDVFilter(django_filters.FilterSet):
    class Meta:
        model = Valeurs
        fields = '__all__'
        exclude = ['datetime','time','temperature','pression','pnt_de_rosée','humidite_absolue','humidite','tension_de_vapeur','pression_cal']

class PresNMFilter(django_filters.FilterSet):
    class Meta:
        model = Valeurs
        fields = '__all__'
        exclude = ['datetime','time','temperature','humidite','pnt_de_rosée','pression','pression_cal','humidite_absolue','tension_de_vapeur','humidite']
