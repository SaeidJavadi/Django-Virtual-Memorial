from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from account.forms import PhoneLoginForm, VerifyCodeForm, RegisterForm
from account.models import User


def LoginPage(request):
    if request.method == 'POST':
        form = PhoneLoginForm(request.POST)
        if form.is_valid():
            phone = f"0{form.cleaned_data['phone']}"
            code = 1234
            # rand_num = randint(1000, 9999)
            # api = KavenegarAPI('54624B564154623558564355506C59417230747550612F7456524A544F4B733535374A624830485856456B3D')
            # params = {'sender':'', 'receptor':phone, 'message':rand_num}
            # api.sms_send(params)
            # return redirect('account:verify', phone, code)
    else:
        form = PhoneLoginForm()
    return render(request, 'account/login.html', {'form': form})


def RegisterPage(request):
    form = RegisterForm(request.POST)
    if form.is_valid():
        print(form.cleaned_data['full_name'])
        return render(request, 'account/register.html', {'form': form})

    return render(request, 'account/register.html', {'form': form})


def verifyPage(request, phone):
    code = 1234
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
    return render(request, 'account/verify.html', {'form': form})
