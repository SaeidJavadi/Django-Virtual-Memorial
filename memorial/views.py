from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import ModelFormMixin
from accounts.models import User
from memorial.forms import Search, DeveasedForm
from memorial.models import *
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.http import JsonResponse, HttpResponse


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


# class DeadDetailView(DetailView):
#     model = Deveased

def DeadView(request, pk):
    marhom = get_object_or_404(Deveased, id=pk)
    context = {}
    btns = {}
    context['deveased'] = marhom
    if marhom.fatehe_chk:
        fatehe_count = Fatehe.objects.all().filter(dead=marhom).count()
        btns['f'] = fatehe_count
    if marhom.salavat_chk:
        salavat_count = Salavat.objects.all().filter(dead=marhom).count()
        btns['s'] = salavat_count
    if marhom.arbain_chk:
        arbain_count = Arbain.objects.all().filter(dead=marhom).count()
        btns['ar'] = arbain_count
    if marhom.ashora_chk:
        ashora_count = Ashora.objects.all().filter(dead=marhom).count()
        btns['ash'] = ashora_count
    if marhom.quran_chk:
        try:
            quran_count = Quran.objects.all().get(dead=marhom).khatm
            quran_dead = Quran.objects.get(dead=marhom)
        except:
            quran_dead = Quran.objects.create(dead=marhom)
            quran_count = quran_dead.khatm
        btns['q'] = quran_count
        btns['joz'] = (quran_dead.j1.all().count(), quran_dead.j2.all().count(), quran_dead.j3.all().count(),
                       quran_dead.j4.all().count(), quran_dead.j5.all().count(), quran_dead.j6.all().count(),
                       quran_dead.j7.all().count(), quran_dead.j8.all().count(), quran_dead.j9.all().count(),
                       quran_dead.j10.all().count(), quran_dead.j11.all().count(), quran_dead.j12.all().count(),
                       quran_dead.j13.all().count(), quran_dead.j14.all().count(), quran_dead.j15.all().count(),
                       quran_dead.j16.all().count(), quran_dead.j17.all().count(), quran_dead.j18.all().count(),
                       quran_dead.j19.all().count(), quran_dead.j20.all().count(), quran_dead.j21.all().count(),
                       quran_dead.j22.all().count(), quran_dead.j23.all().count(), quran_dead.j24.all().count(),
                       quran_dead.j25.all().count(), quran_dead.j26.all().count(), quran_dead.j27.all().count(),
                       quran_dead.j28.all().count(), quran_dead.j29.all().count(), quran_dead.j30.all().count())

    btnCount = len(btns)
    context['btnCount'] = btnCount
    context['btns'] = btns
    return render(request, 'memorial/deveased_detail.html', context)


def vote(request):
    if request.method == 'POST':
        count = 0
        vote = None
        ip = request.META['REMOTE_ADDR']
        marhom_id = request.POST['marhom_id']
        marhom = Deveased.objects.get(id=marhom_id)
        if request.POST['btn'] == 'f':
            vote = Fatehe.objects.create(dead=marhom, ip=ip)
            count = Fatehe.objects.all().filter(dead=marhom).count()
        elif request.POST['btn'] == 's':
            vote = Salavat.objects.create(dead=marhom, ip=ip)
            count = Salavat.objects.all().filter(dead=marhom).count()
        elif request.POST['btn'] == 'ar':
            vote = Arbain.objects.create(dead=marhom, ip=ip)
            count = Arbain.objects.all().filter(dead=marhom).count()
        elif request.POST['btn'] == 'ash':
            vote = Ashora.objects.create(dead=marhom, ip=ip)
            count = Ashora.objects.all().filter(dead=marhom).count()
        if vote:
            response = {
                'status': 'ok',
                'count': count,
            }
            return JsonResponse(response)
    if request.method == 'GET':
        return HttpResponse(
            '<html><head><title>404</title></head><body><center><h1 style="color:blue;font-width=bold">404</h1><h3 style="color:red;">Not Found Page!</h3></center></body></html>')
