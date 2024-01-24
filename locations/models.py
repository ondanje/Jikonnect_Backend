from django.db import models

# Create your models here.

class County(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class SubCounty(models.Model):
    name = models.CharField(max_length=50)
    county=models.ForeignKey(County ,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
  
 

class Locality(models.Model):
    name=models.CharField(max_length=60)
    latitude = models.DecimalField(max_digits=9, decimal_places=6 ,default=0.00)  # Adjust max_digits and decimal_places as needed
    longitude = models.DecimalField(max_digits=9, decimal_places=6,default=0.00)
    subcounty=models.ForeignKey(SubCounty ,related_name='subcounty_Localities',on_delete=models.CASCADE)  
    county=models.ForeignKey(County ,related_name='county_Localities',on_delete=models.CASCADE)    
    is_city=models.BooleanField(default=False)

    def __str__(self):
        return self.name



