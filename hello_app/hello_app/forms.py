from django import forms
from .models import PersonModel

class PersonForm(forms.ModelForm):

    class Meta:
        model=PersonModel
        fields=[
            'title',
            'description'
        ]