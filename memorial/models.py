import jdatetime
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

STATUS_CHOICES = (
    ('active', _('active')),
    ('inactive', _('inactive')),
    ('pending', _('Pending')),
)


class State(models.Model):
    state = models.CharField(max_length=120, verbose_name=_('State'))
    status = models.CharField(max_length=60, choices=STATUS_CHOICES, default='active', verbose_name=_('Status'))

    def __str__(self):
        return self.state

    class Meta:
        verbose_name = _('State')
        verbose_name_plural = _('States')
        ordering = ('id',)


class City(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name=_('ID'), editable=True)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, verbose_name=_('State'))
    city = models.CharField(max_length=120, verbose_name=_('City'))
    status = models.CharField(max_length=60, choices=STATUS_CHOICES, default='active', verbose_name=_('Status'))

    def __str__(self):
        return f"{self.city}"

    class Meta:
        verbose_name = _('City')
        verbose_name_plural = _('Citys')
        ordering = ('id',)
        unique_together =('state', 'city')


class Deveased(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, verbose_name=_('Phone'))
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, verbose_name=_('State'))
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, verbose_name=_('City'))
    picture = models.ImageField(verbose_name=_('Picture'), null=True, blank=True, upload_to='%Y-%m-%d',max_length=200)
    title = models.CharField(max_length=120, verbose_name=_('Title'), null=True, blank=True)
    name = models.CharField(max_length=120, verbose_name=_('Full Name'))
    gender = models.CharField(max_length=7, choices=(('male',_('Male')),('female',_('Female'))), default='male', verbose_name=_('Gender'))
    description = models.TextField(verbose_name=_('Description'), null=True, blank=True)
    address = models.TextField(verbose_name=_('Address'), null=True, blank=True)
    datedied = models.DateField(verbose_name=_('Date died'), null=True, blank=True)
    fatehe_chk = models.BooleanField(verbose_name=_('Fatehe'), default=True)
    salavat_chk = models.BooleanField(verbose_name=_('Salavat'), default=True)
    quran_chk = models.BooleanField(verbose_name=_('Quran'))
    ashora_chk = models.BooleanField(verbose_name=_('Ashora'))
    arbain_chk = models.BooleanField(verbose_name=_('Arbain'))
    ahd_chk = models.BooleanField(verbose_name=_('Ahd'))
    aye_chk = models.BooleanField(verbose_name=_('Aye'))
    Sahifeh_chk = models.BooleanField(verbose_name=_('Sahifeh'))
    komil_chk = models.BooleanField(verbose_name=_('Komil'))
    rabana_chk = models.BooleanField(verbose_name=_('Rabana'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('Created'))
    updated = models.DateTimeField(auto_now=True, verbose_name=_('Updated'))
    status = models.CharField(max_length=60, choices=STATUS_CHOICES, default='active', verbose_name=_('Status'))

    def jd_datedied(self):
        jdatetime.set_locale('fa_IR')
        jdatetime.datetime.now().strftime('%A %B')
        jd_datetime = jdatetime.datetime.fromgregorian(
            year=self.created.year,
            month=self.created.month,
            day=self.created.day,
        )
        return jd_datetime.strftime('%A, %d %B %y %H:%M:%S')

    def __str__(self):
        return f"{self.id} - {self.name}"

    class Meta:
        verbose_name = _('Deveased')
        verbose_name_plural = _('Deveaseds')

    # def get_absolute_url(self):
    #     return reverse('memorial:detail', kwargs={'id': self.id})


class Fatehe(models.Model):
    fatehe = models.ForeignKey(Deveased, on_delete=models.CASCADE, verbose_name=_('Fatehe'))
    ip = models.CharField(max_length=20, verbose_name=_('ip'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.fatehe.id} - {self.fatehe.name}"

    class Meta:
        verbose_name = _('Fatehe')
        verbose_name_plural = _('Fatehe')


class Ashora(models.Model):
    ashora = models.ForeignKey(Deveased, on_delete=models.CASCADE)
    ip = models.CharField(max_length=20, verbose_name=_('ip'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ashora.id} - {self.ashora.name}"

    class Meta:
        verbose_name = _('Ashora')
        verbose_name_plural = _('Ashora')


class Arbain(models.Model):
    arbain = models.ForeignKey(Deveased, on_delete=models.CASCADE, verbose_name=_('Arbain'))
    ip = models.CharField(max_length=20, verbose_name=_('ip'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.arbain.id} - {self.arbain.name}"

    class Meta:
        verbose_name = _('Arbain')
        verbose_name_plural = _('Arbain')


class Ahd(models.Model):
    ahd = models.ForeignKey(Deveased, on_delete=models.CASCADE, verbose_name=_('Ahd'))
    ip = models.CharField(max_length=20, verbose_name=_('ip'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ahd.id} - {self.ahd.name}"

    class Meta:
        verbose_name = _('Ahd')
        verbose_name_plural = _('Ahd')


class Aye(models.Model):
    aye = models.ForeignKey(Deveased, on_delete=models.CASCADE, verbose_name=_('Aye'))
    ip = models.CharField(max_length=20, verbose_name=_('ip'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.aye.id} - {self.aye.name}"

    class Meta:
        verbose_name = _('Aye')
        verbose_name_plural = _('Aye')


class Sahifeh(models.Model):
    sahifeh = models.ForeignKey(Deveased, on_delete=models.CASCADE, verbose_name=_('Sahifeh'))
    ip = models.CharField(max_length=20, verbose_name=_('ip'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sahifeh.id} - {self.sahifeh.name}"

    class Meta:
        verbose_name = _('Sahifeh')
        verbose_name_plural = _('Sahifeh')


class Komil(models.Model):
    komil = models.ForeignKey(Deveased, on_delete=models.CASCADE, verbose_name=_('Komil'))
    ip = models.CharField(max_length=20, verbose_name=_('ip'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.komil.id} - {self.komil.name}"

    class Meta:
        verbose_name = _('Komil')
        verbose_name_plural = _('Komil')


class Rabana(models.Model):
    rabana = models.ForeignKey(Deveased, on_delete=models.CASCADE, verbose_name=_('Rabana'))
    ip = models.CharField(max_length=20, verbose_name=_('ip'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.rabana.id} - {self.rabana.name}"

    class Meta:
        verbose_name = _('Rabana')
        verbose_name_plural = _('Rabana')


class Salavat(models.Model):
    salavat = models.ForeignKey(Deveased, on_delete=models.CASCADE, verbose_name=_('Salavat'))
    ip = models.CharField(max_length=20, verbose_name=_('ip'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.salavat.id} - {self.salavat.name}"

    class Meta:
        verbose_name = _('Salavat')
        verbose_name_plural = _('Salavat')


class Quran(models.Model):
    dead = models.ForeignKey(Deveased, on_delete=models.CASCADE, verbose_name=_('Dead'))
    status = models.CharField(max_length=60, choices=STATUS_CHOICES, default='active', verbose_name=_('Status'))

    def __str__(self):
        return f"{self.dead.id} - {self.dead.name}"

    class Meta:
        verbose_name = _('Quran')
        verbose_name_plural = _('Quran')


class Joz1(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'))

    def __str__(self):
        return f"{self.quran.dead.id}-{self.quran.dead.name}"


class Joze2(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'))

    def __str__(self):
        return f"{self.quran.dead.id}-{self.quran.dead.name}"


class Joze3(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'))

    def __str__(self):
        return f"{self.quran.dead.id}-{self.quran.dead.name}"


class Joze4(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'))

    def __str__(self):
        return f"{self.quran.dead.id}-{self.quran.dead.name}"


class Joze5(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'))

    def __str__(self):
        return f"{self.quran.dead.id}-{self.quran.dead.name}"


class Joze6(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'))

    def __str__(self):
        return f"{self.quran.dead.id}-{self.quran.dead.name}"


class Joze7(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'))

    def __str__(self):
        return f"{self.quran.dead.id}-{self.quran.dead.name}"


class Joze8(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'))

    def __str__(self):
        return f"{self.quran.dead.id}-{self.quran.dead.name}"


class Joze9(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'))

    def __str__(self):
        return f"{self.quran.dead.id}-{self.quran.dead.name}"


class Joze10(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'))

    def __str__(self):
        return f"{self.quran.dead.id}-{self.quran.dead.name}"


class Joze11(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'))

    def __str__(self):
        return f"{self.quran.dead.id}-{self.quran.dead.name}"


class Joze12(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'))

    def __str__(self):
        return f"{self.quran.dead.id}-{self.quran.dead.name}"


class Joze13(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'))

    def __str__(self):
        return f"{self.quran.dead.id}-{self.quran.dead.name}"


class Joze14(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'))

    def __str__(self):
        return f"{self.quran.dead.id}-{self.quran.dead.name}"


class Joze15(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'))

    def __str__(self):
        return f"{self.quran.dead.id}-{self.quran.dead.name}"


class Joze16(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'))

    def __str__(self):
        return f"{self.quran.dead.id}-{self.quran.dead.name}"


class Joze17(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'))

    def __str__(self):
        return f"{self.quran.dead.id}-{self.quran.dead.name}"


class Joze18(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'))

    def __str__(self):
        return f"{self.quran.dead.id}-{self.quran.dead.name}"


class Joze19(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'))

    def __str__(self):
        return f"{self.quran.dead.id}-{self.quran.dead.name}"


class Joze20(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'))

    def __str__(self):
        return f"{self.quran.dead.id}-{self.quran.dead.name}"


class Joze21(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'))

    def __str__(self):
        return f"{self.quran.dead.id}-{self.quran.dead.name}"


class Joze22(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'))

    def __str__(self):
        return f"{self.quran.dead.id}-{self.quran.dead.name}"


class Joze23(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'))

    def __str__(self):
        return f"{self.quran.dead.id}-{self.quran.dead.name}"


class Joze24(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'))

    def __str__(self):
        return f"{self.quran.dead.id}-{self.quran.dead.name}"


class Joze25(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'))

    def __str__(self):
        return f"{self.quran.dead.id}-{self.quran.dead.name}"


class Joze26(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'))

    def __str__(self):
        return f"{self.quran.dead.id}-{self.quran.dead.name}"


class Joze27(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'))

    def __str__(self):
        return f"{self.quran.dead.id}-{self.quran.dead.name}"


class Joze28(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'))

    def __str__(self):
        return f"{self.quran.dead.id}-{self.quran.dead.name}"


class Joze29(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'))

    def __str__(self):
        return f"{self.quran.dead.id}-{self.quran.dead.name}"


class Joze30(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'))

    def __str__(self):
        return f"{self.quran.dead.id}-{self.quran.dead.name}"
