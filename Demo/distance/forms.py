from django import forms

class DistanceForm(forms.Form):
    distance=forms.IntegerField(min_value=1)
    time=forms.TimeField()