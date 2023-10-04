from pyexpat import model
from django import forms
from .models import Rec, Blog


class RecForms(forms.ModelForm):
    class Meta:
        model=Rec
        fields= '__all__'


class BlogForms(forms.ModelForm):
    class Meta:
        model=Blog
        fields= '__all__'