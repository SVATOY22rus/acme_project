from django import forms 

from .models import Birthdey


class BirthdayForm(forms.ModelForm):

    class Meta:
        model = Birthdey
        fields = '__all__'
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }
