from django import forms
from .models import mainman


class hiringform(forms.ModelForm):

    class Meta:
        model=mainman
        fields= '__all__'

        widget = { 'name': forms.TextInput(attrs={'class':'contact'}),
                   'email': forms.TextInput(attrs={'class': 'contact'}),
                   'area_of_expertees': forms.Select(attrs={'class': 'contact'}),
                   'tell_us_about_yourself ': forms.Textarea(attrs={'class': 'contact'}),


        }