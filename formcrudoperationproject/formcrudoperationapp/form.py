from dataclasses import fields
from django import forms

from formcrudoperationapp.models import crud

class crudforms(forms.ModelForm):
    class Meta:
        model=crud
        fields="__all__"