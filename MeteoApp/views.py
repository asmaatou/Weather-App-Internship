from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .filters import *

def valeurs_page(request):
    last_values=Valeurs.objects.last()
    last_value_max_temp=Max_Temp.objects.last()
    last_value_min_temp=Min_Temp.objects.last()
    last_value_max_hum=Max_Hum.objects.last()
    last_value_min_hum=Min_Hum.objects.last()
    last_value_max_pres=Max_Pres.objects.last()
    last_value_min_pres=Min_Pres.objects.last()
    
    context={
        'last_values':last_values,
        'last_value_max_temp':last_value_max_temp,
        'last_value_min_temp':last_value_min_temp,
        'last_value_max_hum':last_value_max_hum,
        'last_value_min_hum':last_value_min_hum,
        'last_value_max_pres':last_value_max_pres,
        'last_value_min_pres':last_value_min_pres
        }
    return render(request,"valeurs.html",context)


def temperature_page(request):
    last_temp=Valeurs.objects.last()
    last_temp_max=Max_Temp.objects.last()
    last_temp_min=Min_Temp.objects.last()
    temp=Valeurs.objects.all().order_by('-id')
    
    myFilter=TempFilter(request.GET, queryset=temp)
    temp = myFilter.qs
    
    labels = []
    data = []
    queryset = Valeurs.objects.order_by('-date')
    for val in queryset:
        labels.append(val.datetime.strftime("%Y-%m-%d %H:%M"))
        data.append(val.temperature)
    context={
        'temp':temp,
        'last_temp':last_temp,
        'labels':labels,
        'data':data,
        'last_temp_max':last_temp_max,
        'last_temp_min':last_temp_min,
        'myFilter':myFilter
        }
    return render(request,"temperature.html",context)


def humidite_page(request):
    last_hum=Valeurs.objects.last()
    last_hum_max=Max_Hum.objects.last()
    last_hum_min=Min_Hum.objects.last()
    hum=Valeurs.objects.all().order_by('-id')
    
    myFilter=HumFilter(request.GET, queryset=hum)
    hum = myFilter.qs
    
    labels = []
    data = []
    queryset = Valeurs.objects.order_by('-time')
    for val in queryset:
        labels.append(val.datetime.strftime("%Y-%m-%d %H:%M"))
        data.append(val.humidite)
    context={
        'hum':hum,
        'last_hum':last_hum,
        'labels':labels,
        'data':data,
        'last_hum_min':last_hum_min,
        'last_hum_max':last_hum_max,
        'myFilter':myFilter
        }
    return render(request,"humidite.html",context)

def pression_page(request):
    last_pres=Valeurs.objects.last()
    last_pres_max=Max_Pres.objects.last()
    last_pres_min=Min_Pres.objects.last()
    pres=Valeurs.objects.all().order_by('-id')
    
    myFilter=PresFilter(request.GET, queryset=pres)
    pres = myFilter.qs
    
    labels = []
    data = []
    queryset = Valeurs.objects.order_by('-time')
    for val in queryset:
        labels.append(val.datetime.strftime("%Y-%m-%d %H:%M"))
        data.append(val.pression)
    context={
        'pres':pres,
        'last_pres':last_pres,
        'labels':labels,
        'data':data,
        'last_pres_min':last_pres_min,
        'last_pres_max':last_pres_max,
        'myFilter':myFilter
        }
    return render(request,"pression.html",context)

def point_de_rosee_page(request):
    last_pnt_de_rosee=Valeurs.objects.last()
    pnt_de_rosee=Valeurs.objects.all().order_by('-id')
    
    myFilter=PointDRFilter(request.GET, queryset=pnt_de_rosee)
    pnt_de_rosee = myFilter.qs
    
    labels = []
    data = []
    queryset = Valeurs.objects.order_by('-time')
    for val in queryset:
        labels.append(val.datetime.strftime("%Y-%m-%d %H:%M"))
        data.append(val.pnt_de_rosée)
    context={
        'last_pnt_de_rosee':last_pnt_de_rosee,
        'pnt_de_rosee':pnt_de_rosee,
        'labels':labels,
        'data':data,
        'myFilter':myFilter
        }
    return render(request,"pointderosee.html",context)

def humidite_absolue_page(request):
    last_hum_abs=Valeurs.objects.last()
    hum_abs=Valeurs.objects.all().order_by('-id')
    
    myFilter=HumAbFilter(request.GET, queryset=hum_abs)
    hum_abs = myFilter.qs
    
    labels = []
    data = []
    queryset = Valeurs.objects.order_by('-time')
    for val in queryset:
        labels.append(val.datetime.strftime("%Y-%m-%d %H:%M"))
        data.append(val.humidite_absolue)
    context={
        'last_hum_abs':last_hum_abs,
        'hum_abs':hum_abs,
        'labels':labels,
        'data':data,
        'myFilter':myFilter
        }
    return render(request,"humiditeabsolue.html",context)

def tension_de_vapeur_page(request):
    last_tens_de_vap=Valeurs.objects.last()
    tens_de_vap=Valeurs.objects.all().order_by('-id')
    
    myFilter=TensionDVFilter(request.GET, queryset=tens_de_vap)
    tens_de_vap = myFilter.qs
    
    labels = []
    data = []
    queryset = Valeurs.objects.order_by('-time')
    for val in queryset:
        labels.append(val.datetime.strftime("%Y-%m-%d %H:%M"))
        data.append(val.tension_de_vapeur)
    context={
        'last_tens_de_vap':last_tens_de_vap,
        'tens_de_vap':tens_de_vap,
        'labels':labels,
        'data':data,
        'myFilter':myFilter
        }
    return render(request,"tensiondevapeur.html",context)

def pression_nv_mer_page(request):
    last_press_cal=Valeurs.objects.last()
    press_cal=Valeurs.objects.all().order_by('-id')
    
    myFilter=PresNMFilter(request.GET, queryset=press_cal)
    press_cal = myFilter.qs
    
    labels = []
    data = []
    queryset = Valeurs.objects.order_by('-time')
    for val in queryset:
        labels.append(val.datetime.strftime("%Y-%m-%d %H:%M"))
        data.append(val.pression_cal)
    context={
        'last_press_cal':last_press_cal,
        'press_cal':press_cal,
        'labels':labels,
        'data':data,
        'myFilter':myFilter
        }
    return render(request,"pressionnvmer.html",context)

def metar_page(request):
    last_values=Valeurs.objects.last()
    context={
        'last_values':last_values
    }
    return render(request,"metar.html",context)

def synop_page(request):
    last_values=Valeurs.objects.last()
    context={
        'last_values':last_values
    }
    return render(request,"synop.html",context)

def speci_page(request):

    return render(request,"speci.html")






