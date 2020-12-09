from django import forms
from django.utils.translation import gettext_lazy as _
from memorial.models import Deveased

searchD = {'class': 'form-control', 'placeholder': _('Deveased Code'), 'dir': 'rtl'}


class Search(forms.Form):
    search = forms.CharField(max_length=200, label='', widget=forms.TextInput(attrs=searchD), )


class DeveasedForm(forms.ModelForm):
    class Meta:
        model = Deveased
        fields = (
        'state', 'city', 'picture', 'title', 'name', 'description', 'address', 'datedied', 'quran_chk', 'fatehe_chk',
        'ashora_chk',
        'arbain_chk', 'ahd_chk', 'aye_chk', 'Sahifeh_chk', 'komil_chk', 'rabana_chk')
        widgets = {
            'state': forms.Select(attrs={'class': 'form-control', 'onChange': 'iranwebsv(this.value);'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'picture': forms.FileInput(attrs={'class': 'form-control-file border'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'datedied': forms.DateInput(attrs={'class': 'form-control'},)
            # 'quran_chk':forms.CheckboxInput(attrs={'class':'custom-control-input','type':'checkbox'}),
        }
        labels = {
            'title': 'عنوان (مانند شادروان)',
            'address': 'آدرس آرمگاه:',
            'Sahifeh_chk': 'دعای 7 صحیفه سجادیه'
        }

    def __init__(self, *args, **kwargs):
        super(DeveasedForm, self).__init__(*args, **kwargs)
        self.fields['state'].empty_label = 'لطفا استان را انتخاب نمایید'
        YEAR_CHOICES = range(1400, 1250, -1)
        MONTH_CHOICES = {1: 'فروردین', 2: 'اردیبهشت', 3: 'خرداد', 4: 'تیر', 5: 'مرداد', 6: 'شهریور', 7: 'مهر',
                         8: 'آبان', 9: 'آذر', 10: 'دی', 11: 'بهمن', 12: 'اسفند'}
        self.fields['datedied'] = forms.DateField(required=False,
                                                  widget=forms.SelectDateWidget(empty_label=['سال', 'ماه', 'روز'],
                                                                                years=YEAR_CHOICES,
                                                                                months=MONTH_CHOICES))
