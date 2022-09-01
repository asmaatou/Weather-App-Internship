from django.urls import path
from . import views

urlpatterns = [
    path('',views.valeurs_page,name="valeurs"),
    path('temperature/',views.temperature_page,name="temperature"),   
    path('humidite/',views.humidite_page,name="humidite"),
    path('pression/',views.pression_page,name="pression"),
    path('point_de_rosée/',views.point_de_rosee_page,name="point_de_rosee"),   
    path('humidite_absolue/',views.humidite_absolue_page,name="humidite_absolue"),
    path('tension_de_vapeur/',views.tension_de_vapeur_page,name="tension_de_vapeur"),
    path('pression_nv_mer/',views.pression_nv_mer_page,name="pression_nv_mer"),
    path('metar/',views.metar_page,name="Metar"),
    path('synop/',views.synop_page,name="Synop"),
    path('speci/',views.speci_page,name="Speci"),
]
