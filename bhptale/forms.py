from django import forms
from bhptale.models import UserRole
from bhptale.models import RoleOne

class UserRoleForm(forms.ModelForm):
    class Meta():
        model=UserRole
        #fields=' all '
        exclude=["role_id","role_name"]
        #include