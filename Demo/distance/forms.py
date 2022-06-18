from turtle import distance
from django import forms
 
# creating a form
class DistanceForm(forms.Form):
    distance = forms.IntegerField()
    time = forms.TimeField(input_formats=['%I:%M %p'])