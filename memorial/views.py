from django.shortcuts import render
from django.urls import reverse_lazy
from memorial.forms import Search
from memorial.models import Deveased
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView


def home(request):
    form = Search()
    return render(request, 'memorial/home.html', {'form': form})


@login_required
def dashboard(request):
    return render(request, 'memorial/dashboard.html', {})


class DeveasedCreate(CreateView):
    model = Deveased
    fields = ('city', 'picture', 'title', 'fname', 'lname', 'description', 'address', 'quran_chk', 'fatehe_chk', 'ashora_chk',
        'arbain_chk', 'ahd_chk', 'aye_chk', 'Sahifeh_chk', 'komil_chk', 'rabana_chk')
    template_name = 'memorial/deveasedـcreate.html'
    success_url = reverse_lazy('memorial:home')
