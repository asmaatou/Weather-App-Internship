from django.db import models

# Create your models here.

class Valeurs(models.Model):
    datetime=models.DateTimeField(null=True)
    date=models.DateField(null=True)
    time=models.TimeField(null=True)
    temperature=models.FloatField()
    humidite=models.FloatField()
    pression=models.FloatField()
    pnt_de_rosée=models.FloatField()
    humidite_absolue=models.FloatField()
    tension_de_vapeur=models.FloatField()
    pression_cal=models.FloatField()
    
    def __str__(self):
        return self.date
    
class Min_Temp(models.Model):
    date=models.DateField(null=True)
    time=models.TimeField(null=True)
    temp_min=models.FloatField(null=True)
    
    def __str__(self):
        return self.date
    
class Max_Temp(models.Model):
    date=models.DateField(null=True)
    time=models.TimeField(null=True)
    temp_max=models.FloatField(null=True)
    
    def __str__(self):
        return self.date
    
class Min_Hum(models.Model):
    date=models.DateField(null=True)
    time=models.TimeField(null=True)
    hum_min=models.FloatField(null=True)
    
    def __str__(self):
        return self.date
    
class Max_Hum(models.Model):
    date=models.DateField(null=True)
    time=models.TimeField(null=True)
    hum_max=models.FloatField(null=True)
    
    def __str__(self):
        return self.date
    
class Min_Pres(models.Model):
    date=models.DateField(null=True)
    time=models.TimeField(null=True)
    pres_min=models.FloatField(null=True)
    
    def __str__(self):
        return self.date
    
class Max_Pres(models.Model):
    date=models.DateField(null=True)
    time=models.TimeField(null=True)
    pres_max=models.FloatField(null=True)
    
    def __str__(self):
        return self.date
    