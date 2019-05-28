from django.db import models

# Create your models here.
class SignUpRole(models.Model):
    role_id=models.AutoField(primary_key=True)
    role_username=models.CharField(max_length=225,
                               default="",
                               unique=True)
    role_email=models.EmailField(unique=True)
    role_password=models.CharField(unique=True,
                                   max_length=225,)

#after this run these commands
#python manage.py makemigrations appname
#python manage.py migrate