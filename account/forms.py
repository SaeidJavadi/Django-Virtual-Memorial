from django import forms
from account.models import User
from django.utils.translation import gettext_lazy as _

msgError = {
    'required': _('This field is required'),
    'invalid': _('The value entered is invalid'),
    'max_value': _('The value entered is set above the ceiling'),
    'min_value': _('The value entered is less than the specified limit')
}

phoneFieldAttrs ={'class': 'form-control', 'placeholder': '09 - - - - - - - - -', 'type': 'tel', 'maxlength': '14','minlength':'11'}

class PhoneLoginForm(forms.Form):
    phone = forms.IntegerField(error_messages=msgError, widget=forms.NumberInput(
        attrs=phoneFieldAttrs))

    def clean_phone(self):
        phone = User.objects.filter(phone=self.cleaned_data['phone'])
        if not phone.exists():
            # raise forms.ValidationError(_('This phone number does not exists'))
            # phone = User.objects.create_user()
            pass
        return self.cleaned_data['phone']


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('phone', 'full_name','password')
        widgets = {
            'phone': forms.NumberInput(
                attrs=phoneFieldAttrs),
            'full_name':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name',}),
            'password':forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Code',}),
        }
        labels = {
            'password':_('Your Code'),
        }
        # help_texts = {
        #     'phone': _('Some useful help text.'),
        # }
        # error_messages = {
        #     'phone': {
        #         'max_length': _("This writer's name is too long."),
        #     },
        # }


class VerifyCodeForm(forms.Form):
    code = forms.IntegerField()
