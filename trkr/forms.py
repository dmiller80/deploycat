from django import forms
from .models import *

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('name', 'nick_name', 'address', 'city', 'state', 'zipcode', 'email', 'cell_phone',
                   )
    date = forms.DateField(
        widget=forms.TextInput(attrs={'type': 'date'}))

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ('name', 'cal_minute', 'note', )

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ('client', 'type', 'duration', 'note', )
    date = forms.DateField(
        widget=forms.TextInput(attrs={'type': 'date'})
    )

class NameForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ('client', 'type', 'duration', 'note', )
    your_name = forms.CharField(label='Your name', max_length=100)
    date = forms.DateField(
        widget=forms.TextInput(attrs={'type': 'date'})
    )

