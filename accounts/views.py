from random import randint
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from accounts.forms import PhoneLoginForm, VerifyCodeForm, RegisterForm
from accounts.models import User
from django.utils.translation import gettext_lazy as _
from kavenegar import *

def LoginPage(request):
    if request.method == 'POST':
        global code, phone
        form = PhoneLoginForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone']
            if User.objects.filter(phone=phone).exists():
                request.session['phone'] = f"0{phone}"
                return redirect('accounts:verify')
            else:
                phone = f"0{phone}"
                code = str(randint(1000, 9999))
                # code = str(1234)
                text = f"""«سامانه یادبود مجازی»
رمزعبور عضویت شما:
{code}""".encode('utf-8')
                api = KavenegarAPI('706D423758354D2B485652432B436C324F34412B454D59493549686234414534413157777178726D30486F3D')
                params = {'sender':'1000596446', 'receptor':phone, 'message':text}
                response = api.sms_send(params)
                print(response)
                print('+'*10,'New Code','+'*10)
                print(code)
                print('+'*10,'New Code','+'*10)
                request.session['phone'] = f"0{phone}"
                request.session['code'] = code
                messages.success(request, _('The login password was sent to your number.'),'info')
                return redirect('accounts:register')


    else:
        form = PhoneLoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def RegisterPage(request):
    form = RegisterForm()
    # phone = request.session['phone']
    # code = request.session['code']
    form.fields['phone'].initial = phone
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            if password == code:
                user = User.objects.create_user(phone=form.cleaned_data['phone'],
                                                name=form.cleaned_data['name'],
                                                password=password)
                user.save()
                login(request, user)
                return redirect('memorial:dashboard')
            else:
                messages.error(request, _('The code entered is incorrect'), 'warning')
                print('error code')
    return render(request, 'accounts/register.html', {'form': form})


def VerifyPage(request):
    if request.method == 'POST':
        form = VerifyCodeForm(request.POST)
        phone = request.session['phone']
        print(phone)
        if form.is_valid():
            user = authenticate(request, username=phone, password=form.cleaned_data['code'])
            if user:
                login(request, user)
                messages.success(request, _('logged in successfully'), 'success')
                return redirect('memorial:dashboard')
            else:
                messages.error(request, _('your code is wrong'), 'warning')
    else:
        form = VerifyCodeForm()
    return render(request, 'accounts/verify.html', {'form': form})


def LogoutPage(request):
    logout(request)
    messages.success(request, _('you logged out successfully'), 'success')
    return redirect('memorial:home')