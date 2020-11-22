from random import randint

from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from accounts.forms import PhoneLoginForm, VerifyCodeForm, RegisterForm
from accounts.models import User
from django.utils.translation import gettext_lazy as _



def LoginPage(request):
    if request.method == 'POST':
        global code , phone
        form = PhoneLoginForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone']
            if User.objects.filter(phone=phone).exists():
                return redirect('accounts:verify')
            else:
                phone = f"0{phone}"
                # code = str(randint(1000, 9999))
                code = str(1234)
                print('+'*10,'New Code','+'*10)
                print(code)
                print('+'*10,'New Code','+'*10)
                # api = KavenegarAPI('54624B564154623558564355506C59417230747550612F7456524A544F4B733535374A624830485856456B3D')
                # params = {'sender':'', 'receptor':phone, 'message':rand_num}
                # api.sms_send(params)
                # request.session['phone'] = f"0{phone}"
                # request.session['code'] = code
                # messages.success(request, _('The login password was sent to your number.'),'info')
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
                user = User.objects.create_user(phone=form.cleaned_data['phone'], full_name=form.cleaned_data['full_name'],
                                                password=password)
                user.save()
                return redirect('accounts:login')
            else:
                messages.error(request, 'The code entered is incorrect', 'warning')
                print('error code')
    return render(request, 'accounts/register.html', {'form': form})


def VerifyPage(request):
    code = 1234
    phone = 0
    if request.method == 'POST':
        form = VerifyCodeForm(request.POST)
        if form.is_valid():
            if code == form.cleaned_data['code']:
                profile = get_object_or_404(User, phone=phone)
                user = get_object_or_404(User, profile__id=profile.id)
                login(request, user)
                messages.success(request, 'logged in successfully', 'success')
                return redirect('posts:all_posts')
            else:
                messages.error(request, 'your code is wrong', 'warning')
    else:
        form = VerifyCodeForm()
    return render(request, 'accounts/verify.html', {'form': form})
