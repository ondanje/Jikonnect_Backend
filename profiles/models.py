from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError


def upload_location(instance, filename):
    file_path = 'profiles/{user_id}{first_name}/-{filename}'.format(
        user_id=str(instance.user.id), first_name=str(instance.first_name), filename=filename)
    return file_path




# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.PROTECT)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    id_number=models.CharField(max_length=12,null=True, blank=True,)
    id_field=models.FileField(upload_to=upload_location, null=True, blank=True,verbose_name="ID ATTACHMENT")
    #is_complete=models.BooleanField(default= False)
    verified=models.BooleanField(default=False)


    @property
    def phone_number(self):
        return self.user.phone_number if self.user.phone_number else None

    



    def __str__(self):
        fullname=f'{self.first_name} {self.last_name}'
        return f'profile email:{self.user.email} '
    


   


