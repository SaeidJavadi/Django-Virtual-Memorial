from django.shortcuts import render
from memorial.forms import Search
from django.contrib.auth.decorators import login_required


def home(request):
    form = Search()
    return render(request,'memorial/home.html', {'form':form})

@login_required
def dashboard(request):
    return render(request,'memorial/dashboard.html',{})


