from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from accounts.models import User
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

msgError = {
    'required': _('This field is required'),
    'invalid': _('The value entered is invalid'),
    'max_value': _('The value entered is set above the ceiling'),
    'min_value': _('The value entered is less than the specified limit')
}

phoneFieldAttrs = {'class': 'form-control', 'placeholder': '09 - - - - - - - - -', 'type': 'tel', 'maxlength': '14',
                   'minlength': '11'}


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
        fields = ('phone', 'full_name', 'password')
        widgets = {
            'phone': forms.NumberInput(
                attrs=phoneFieldAttrs),
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name', }),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Code', }),
        }
        labels = {
            'password': _('Your Code'),
        }
        # help_texts = {
        #     'phone': _('Some useful help text.'),
        # }
        # error_messages = {
        #     'phone': {
        #         'max_length': _("This writer's name is too long."),
        #     },
        # }
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


# class UserCreationForm(forms.ModelForm):
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
#
#     class Meta:
#         model = User
#         fields = ('phone', 'full_name')
#
#     def clean_password2(self):
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise ValidationError("Passwords don't match")
#         return password2
#
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data["password1"])
#         if commit:
#             user.save()
#         return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('phone', 'full_name', 'password', 'is_active', 'is_admin')

    def clean_password(self):
        return self.initial["password"]


class VerifyCodeForm(forms.Form):
    code = forms.IntegerField()
