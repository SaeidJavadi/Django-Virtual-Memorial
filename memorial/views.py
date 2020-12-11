from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import ModelFormMixin
from accounts.models import User
from memorial.forms import Search, DeveasedForm
from memorial.models import Deveased
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


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
    error_message = 'خطا در ورود اطلاعات'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        messages.success(self.request, self.success_message)
        return super(ModelFormMixin, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, self.error_message)
        return super().form_invalid(form)


@login_required
def list(request):
    user = User.objects.get(phone=request.user.phone)
    dead = Deveased.objects.filter(user=user).order_by('-updated')
    allObj = dead.count()
    paginator = Paginator(dead, 5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'memorial/deveased_list.html', {'objects': posts, 'allObj': allObj})


@login_required
def delete(request, id=None):
    dead = get_object_or_404(Deveased, pk=id)
    if dead.delete():
        messages.success(request, _('item deleted successfully!'), extra_tags='alert alert-warning')
    return render(request, 'memorial/delete.html', {'marhom': dead})


def DeveasedEdit(request, id=None):
    instance = get_object_or_404(Deveased, id=id)
    form = DeveasedForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        form.save()
        messages.success(request, _('updated successfully!!'), extra_tags='alert alert-success')
        # return HttpResponseRedirect(instance.get_absolute_url())
        return redirect('memorial:list_Deveased')
    context = {
        'form': form,
    }
    # import ipdb; ipdb.set_trace()
    return render(request, 'memorial/deveased_edit.html', context)
