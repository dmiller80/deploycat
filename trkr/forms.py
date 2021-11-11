from django import forms
from .models import *

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('name', 'nick_name', 'address', 'city', 'state', 'zipcode', 'email', 'cell_phone',
                  'birth_date', )

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ('name', 'cal_minute', 'note', )

