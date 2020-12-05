from django import forms
from django.utils.translation import gettext_lazy as _

searchD = {'class': 'form-control', 'placeholder': 'Search'}

class Search(forms.Form):
    search = forms.CharField(max_length=200, label='', widget=forms.TextInput(attrs=searchD))