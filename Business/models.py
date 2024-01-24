from django.db import models
from django.db import models
from locations.models import Locality
from  profiles.models import  Profile
from django.core.validators import FileExtensionValidator
from django.core.validators import RegexValidator


def upload_location(instance, filename):
    file_path = 'business/{user_id}/{first_name}/{id_number}-{filename}'.format(
        user_id=str(instance.owner.id),id_number=str(instance.id_number), first_name=str(instance.owner.first_name), filename=filename)
    return file_path



    
# # # class  Industry(models.Model):
# # #     name=models.CharField(max_length= 255)

# # #     def __str__(self):
# # #         return self.name



class Business(models.Model):
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    name = models.CharField(max_length=60)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    email = models.EmailField(max_length=120)
    website = models.URLField(null=True, blank=True)    
    description = models.TextField(max_length=200)
    industry = models.CharField(max_length=100)
    founded_in = models.DateTimeField(null=True, blank=True,)
    employee_count = models.PositiveIntegerField() 
    id_number=models.CharField(max_length= 13,verbose_name="ID Number")
    kra_pin = models.CharField(max_length = 42 ,verbose_name="kra pin number",null=True, blank=True,)
    bs_reg_number=models.CharField(max_length=100 ,null=True, blank=True,verbose_name='Business registration number')   
    bs_permit_number=models.CharField(max_length=100,verbose_name="Business Permit Number",null=True, blank=True,)
    ceritificate_of_registration = models.FileField(upload_to=None, validators=[FileExtensionValidator(['pdf'])], max_length = 100,null=False,blank=False,)
    id_attachment = models.FileField(upload_to=None, validators=[FileExtensionValidator(['pdf'])], max_length = 100,null=False,blank=False,default="not available")    
    business_permit = models.FileField(upload_to=upload_location,  validators=[FileExtensionValidator(['pdf'])],  max_length = 100,null=True, blank=True,)
    kra_pin_attachment = models.FileField(upload_to=None, validators=[FileExtensionValidator(['pdf'])], max_length = 100,null=True, blank=True,)     
    social_media_links = models.JSONField(null=True, blank=True,default=dict)
    owner= models.ForeignKey(Profile, on_delete=models.PROTECT)
    locality = models.ForeignKey(Locality, related_name='businesses', on_delete=models.CASCADE)
    is_verified = models.BooleanField(default=False)
    is_top_rated=models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    
    
    def __str__(self):
        return self.name
    
