from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import ModelFormMixin
from memorial.forms import Search, DeveasedForm
from memorial.models import Deveased
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin


def home(request):
    form = Search()
    return render(request, 'memorial/home.html', {'form': form})


@login_required
def dashboard(request):
    return render(request, 'memorial/dashboard.html', {})


class DeveasedCreate(LoginRequiredMixin, CreateView):
    model = Deveased
    form_class = DeveasedForm
    template_name = 'memorial/deveased_create.html'
    success_url = reverse_lazy('memorial:dashboard')
    success_message = 'با موفقیت اضافه شد'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super(ModelFormMixin, self).form_valid(form)
