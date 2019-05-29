from django.db import models

# Create your models here
class UserRole(models.Model):
    id=models.AutoField(primary_key=True)
    role=models.CharField(max_length=225,unique=True,default="")
    def __str__(self):
        return self.role


#after this run these commands
#python manage.py makemigrations appname
#python manage.py migrate