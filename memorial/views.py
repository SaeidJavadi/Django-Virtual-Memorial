from django.shortcuts import render
from memorial.forms import Search


def home(request):
    form = Search()
    return render(request,'memorial/home.html', {'form':form})


