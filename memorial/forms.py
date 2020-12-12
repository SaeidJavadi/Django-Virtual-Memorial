from django import forms
from django.utils.translation import gettext_lazy as _
from memorial.models import Deveased
from pytz import timezone
from jdatetime import datetime as dt

searchD = {'class': 'form-control', 'placeholder': _('Deveased Code'), 'dir': 'rtl'}


class Search(forms.Form):
    search = forms.CharField(max_length=200, label='', widget=forms.TextInput(attrs=searchD), )


class DeveasedForm(forms.ModelForm):
    class Meta:
        model = Deveased
        fields = (
            'state', 'city', 'picture', 'title', 'name', 'gender', 'description', 'address', 'datedied', 'quran_chk',
            'fatehe_chk',
            'ashora_chk',
            'arbain_chk', 'ahd_chk', 'aye_chk', 'Sahifeh_chk', 'komil_chk', 'rabana_chk')
        widgets = {
            'state': forms.Select(attrs={'class': 'form-control', 'onChange': 'iranwebsv(this.value);'}),
            'city': forms.Select(attrs={'class': 'form-control'}),
            'picture': forms.FileInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'datedied': forms.DateInput(attrs={'class': 'form-control'}),
            # 'quran_chk':forms.CheckboxInput(attrs={'class':'customInput-control-input','type':'checkbox'}),
        }
        labels = {
            'title': 'عنوان (مانند شادروان)',
            'address': 'آدرس آرمگاه:',
            'Sahifeh_chk': 'دعای 7 صحیفه سجادیه',
            'description':'توضیحات مندرج در ذیل صفحه'
        }
        forceInputField = 'این فیلد اجباری است'
        error_messages = {
            'state': {
                'required': forceInputField,
            },
            'city': {
                'required': forceInputField,
            },
            'name': {
                'required': forceInputField,
            }
        }
        help_texts = {
            'state': 'ابتدا استان مورد نظر را انتخاب کید',
            'name': 'نام مرحوم را وارد کنید'
        }

    def __init__(self, *args, **kwargs):
        super(DeveasedForm, self).__init__(*args, **kwargs)
        self.fields['state'].empty_label = 'لطفا استان را انتخاب نمایید'
        self.fields['city'].empty_label = 'لطفا ابتدا استان را انتخاب نمایید'
        tz = timezone('Asia/Tehran')
        timDel = dt.now(tz)
        # DateNow = timDel.strftime("%Y/%m/%d %H:%M:%S")
        YearNow = int(timDel.strftime("%Y"))
        YEAR_CHOICES = range(YearNow, 1249, -1)
        MONTH_CHOICES = {1: 'فروردین', 2: 'اردیبهشت', 3: 'خرداد', 4: 'تیر', 5: 'مرداد', 6: 'شهریور', 7: 'مهر',
                         8: 'آبان', 9: 'آذر', 10: 'دی', 11: 'بهمن', 12: 'اسفند'}
        self.fields['datedied'] = forms.DateField(required=False,
                                                  widget=forms.SelectDateWidget(empty_label=['سال', 'ماه', 'روز'],
                                                                                years=YEAR_CHOICES,
                                                                                months=MONTH_CHOICES))
