from django.db import models

# Create your models here
class UserRole(models.Model):
    id=models.AutoField(primary_key=True)
    role=models.CharField(max_length=225,
                          unique=True,
                          default="")
    def __str__(self):
        return self.role
class RoleDetails(models.Model):
    role=models.ForeignKey(UserRole,
                           on_delete=models.CASCADE)
    email=models.CharField(primary_key=True,
                           max_length=255,
                           default="")
    password=models.CharField(max_length=225,
                              default="")

    username=models.CharField(unique=True,
                              null=True,
                              max_length=255,
                              default="")
    fullname=models.CharField(max_length=225,
                              null=True,
                              default="")
    mobile=models.BigIntegerField(unique=True,
                                  default="")
    address=models.CharField(max_length=225,
                             null=True,
                             default="")
    gender=models.CharField(max_length=10,
                            null=True,
                            default="")
    otp=models.CharField(max_length=255,
                         null=True,
                         default="")
    otp_time=models.CharField(max_length=255,
                              null=True,
                              default="")
    verify_link=models.CharField(max_length=255,
                                 null=True,
                                 default="")
    active=models.NullBooleanField(default="")
    last_login=models.CharField(default="",
                                null=True,
                                max_length=255)


#after this run these commands
#python manage.py makemigrations appname
#python manage.py migrate