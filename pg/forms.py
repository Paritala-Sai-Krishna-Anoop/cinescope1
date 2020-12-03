from django import forms
from .models import mainman , join , UploadFile
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm
from django.contrib.auth.models import User

class hiringform(forms.ModelForm):

    class Meta:
        model=mainman
        fields= '__all__'
        name = forms.CharField(widget=forms.TextInput(attrs={
            "class": "input",
            "type": "text",
            "placeholder": "enter username"
        }))

        widget = { 'name': forms.TextInput(attrs={'class':'contact'}),
                   'email': forms.TextInput(attrs={'class': 'contact'}),
                   'area_of_expertees': forms.Select(attrs={'class': 'contact'}),
                   'tell_us_about_yourself ': forms.Textarea(attrs={'class': 'contact'}),


        }
class joiningform(forms.ModelForm):

    class Meta:
        model=join
        fields='__all__'

class CreateUserform(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class":"input",
        "type":"text",
        "placeholder":"enter username"
    }))
    email = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "email",
        "placeholder": "enter your email"
    }))
    password1 = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "password",
        "placeholder": "enter password"
    }))
    password2 = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "password",
        "placeholder": "re-enter password"
    }))


    class Meta:
        model=User
        fields=['username','email','password1','password2']


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadFile
        fields = '__all__'