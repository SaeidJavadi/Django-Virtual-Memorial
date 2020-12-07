from django import forms
from django.utils.translation import gettext_lazy as _

from memorial.models import Deveased

searchD = {'class': 'form-control', 'placeholder': _('Deveased Code'),'dir':'rtl'}

class Search(forms.Form):
    search = forms.CharField(max_length=200, label='', widget=forms.TextInput(attrs=searchD), )

class DeveasedForm(forms.ModelForm):
    class Meta:
        model = Deveased
        fields = ('state','city', 'picture', 'title', 'fname', 'lname', 'description', 'address', 'quran_chk', 'fatehe_chk', 'ashora_chk',
            'arbain_chk', 'ahd_chk', 'aye_chk', 'Sahifeh_chk', 'komil_chk', 'rabana_chk')
        widgets = {
            'state':forms.Select(attrs={'class':'form-control'}),
            'city':forms.Select(attrs={'class':'form-control'}),
            'picture':forms.FileInput(attrs={'class':'form-control-file border'}),
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'fname':forms.TextInput(attrs={'class':'form-control'}),
            'lname':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            # 'quran_chk':forms.CheckboxInput(attrs={'class':'custom-control-input','type':'checkbox'}),

        }
        labels = {
            'title': 'عنوان (مانند شادروان):',
            'address': 'آدرس آرمگاه:',
            'Sahifeh_chk':'دعای 7 صحیفه سجادیه'
        }