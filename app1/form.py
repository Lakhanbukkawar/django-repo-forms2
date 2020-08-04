from django import forms

class student(forms.Form):
    name=forms.CharField(max_length=30,required=False)