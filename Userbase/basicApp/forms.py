from django import forms
from django.contrib.auth.models import User
from basicApp.models import AddOnFieldsTo_User


class Existing_User_Form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email' , 'password')

class Addon_Form(forms.ModelForm):
    class Meta():
        model = AddOnFieldsTo_User
        fields = ('portfolio', 'DP')

