from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from accounts.forms import PhoneLoginForm, VerifyCodeForm, RegisterForm
from accounts.models import User
from django.utils.translation import gettext_lazy as _
from accounts.tasks import send_sms


def LoginPage(request):
    if request.method == 'POST':
        global code, phone
        form = PhoneLoginForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone']
            if User.objects.filter(phone=phone).exists():
                request.session['phone'] = f"{phone}"
                return redirect('accounts:verify')
            else:
                # code = str(randint(1000, 9999))
                code = "1234"
                phone = f"{phone}"
                try:
                    code = send_sms(phone,code)
                except:
                    code = "1234"
                if code:
                    print(code)
                    request.session['phone'] = phone
                    request.session['code'] = code
                    messages.success(request, _('The login password was sent to your number.'), 'info')
                    return redirect('accounts:register')
                else:
                    messages.error(request, _('در ارسال رمزعبور مشکلی پیش آمده است، لطفا لحظات دیگری تلاش کنید'),
                                   'warning')
                    return redirect('accounts:login')
    else:
        form = PhoneLoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def ForgetPage(request):
    if request.method == 'POST':
        global code, phone
        form = PhoneLoginForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone']
            # code = str(randint(1000, 9999))
            code = "1234"
            phone = f"{phone}"
            try:
                code = send_sms(phone,code)
            except:
                code = "1234"
            if code:
                request.session['phone'] = phone
                request.session['code'] = code
                user = User.objects.get(phone=int(phone))
                user.set_password(code)
                user.save()
                messages.success(request, _('The login password was sent to your number.'), 'info')
                return redirect('accounts:verify')
            else:
                messages.error(request, _('در ارسال رمزعبور مشکلی پیش آمده است، لطفا لحظات دیگری تلاش کنید'),
                               'warning')
                return redirect('accounts:forget')
    else:
        form = PhoneLoginForm()
    return render(request, 'accounts/forget.html', {'form': form})

def RegisterPage(request):
    form = RegisterForm()
    phone = request.session['phone']
    code = request.session['code']
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
