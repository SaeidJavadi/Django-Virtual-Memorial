from django.db import models
from django.utils.translation import gettext_lazy as _

STATUS_CHOICES = (
    ('active', _('active')),
    ('inactive', _('inactive'))
)


class Deveased(models.Model):
    user_phone = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    state = models.CharField(max_length=100, verbose_name=_('State'), null=True, blank=True)
    city = models.CharField(max_length=100, verbose_name=_('City'), null=True, blank=True)
    picture = models.ImageField(verbose_name=_('Picture'), null=True, blank=True)
    title = models.CharField(max_length=120, verbose_name=_('Title'), null=True, blank=True)
    fname = models.CharField(max_length=120, verbose_name=_('First Name'), null=True, blank=True)
    lname = models.CharField(max_length=120, verbose_name=_('Last Name'), null=True, blank=True)
    description = models.TextField(verbose_name=_('Description'), null=True, blank=True)
    address = models.TextField(verbose_name=_('Address'), null=True, blank=True)
    quran_chk = models.BooleanField(verbose_name=_('Quran'))
    fatehe_chk = models.BooleanField(verbose_name=_('fatehe'))
    ashora_chk = models.BooleanField(verbose_name=_('ashora'))
    arbain_chk = models.BooleanField(verbose_name=_('arbain'))
    ahd_chk = models.BooleanField(verbose_name=_('ahd'))
    aye_chk = models.BooleanField(verbose_name=_('aye'))
    sahife_chk = models.BooleanField(verbose_name=_('sahife'))
    komil_chk = models.BooleanField(verbose_name=_('komil'))
    rabana_chk = models.BooleanField(verbose_name=_('rabana'))
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=60, choices=STATUS_CHOICES, default='active', verbose_name=_('Status'))

    def __str__(self):
        return self.fname + " " + self.lname

    class Meta:
        verbose_name = _('Deveased')
        verbose_name_plural = _('Deveaseds')


class Fatehe(models.Model):
    fatehe = models.ForeignKey(Deveased, on_delete=models.CASCADE)
    ip = models.CharField(max_length=20, verbose_name=_('ip'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fatehe.fname + ' ' + self.fatehe.lname

    class Meta:
        verbose_name = _('Fatehe')
        verbose_name_plural = _('Fatehe')


class Ashora(models.Model):
    ashora = models.ForeignKey(Deveased, on_delete=models.CASCADE)
    ip = models.CharField(max_length=20, verbose_name=_('ip'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ashora.fname + ' ' + self.ashora.lname

    class Meta:
        verbose_name = _('Ashora')
        verbose_name_plural = _('Ashora')


class Arbain(models.Model):
    arbain = models.ForeignKey(Deveased, on_delete=models.CASCADE)
    ip = models.CharField(max_length=20, verbose_name=_('ip'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.arbian.fname + ' ' + self.arbian.lname

    class Meta:
        verbose_name = _('Arbain')
        verbose_name_plural = _('Arbain')


class Ahd(models.Model):
    ahd = models.ForeignKey(Deveased, on_delete=models.CASCADE)
    ip = models.CharField(max_length=20, verbose_name=_('ip'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ahd.fname + ' ' + self.ahd.lname

    class Meta:
        verbose_name = _('Ahd')
        verbose_name_plural = _('Ahd')


class Aye(models.Model):
    aye = models.ForeignKey(Deveased, on_delete=models.CASCADE)
    ip = models.CharField(max_length=20, verbose_name=_('ip'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.aye.fname + ' ' + self.aye.lname

    class Meta:
        verbose_name = _('Aye')
        verbose_name_plural = _('Aye')


class Sahifeh(models.Model):
    sahifeh = models.ForeignKey(Deveased, on_delete=models.CASCADE)
    ip = models.CharField(max_length=20, verbose_name=_('ip'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sahifeh.fname + ' ' + self.sahifeh.lname

    class Meta:
        verbose_name = _('Sahifeh')
        verbose_name_plural = _('Sahifeh')


class Komil(models.Model):
    komil = models.ForeignKey(Deveased, on_delete=models.CASCADE)
    ip = models.CharField(max_length=20, verbose_name=_('ip'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.komil.fname + ' ' + self.komil.lname

    class Meta:
        verbose_name = _('Komil')
        verbose_name_plural = _('Komil')


class Rabana(models.Model):
    rabana = models.ForeignKey(Deveased, on_delete=models.CASCADE)
    ip = models.CharField(max_length=20, verbose_name=_('ip'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.rabana.fname + ' ' + self.rabana.lname

    class Meta:
        verbose_name = _('Rabana')
        verbose_name_plural = _('Rabana')


class Quran(models.Model):
    dead = models.ForeignKey(Deveased, on_delete=models.CASCADE)
    joze1 = models.BooleanField(verbose_name=_('joze 1'))
    joze2 = models.BooleanField(verbose_name=_('joze 2'))
    joze3 = models.BooleanField(verbose_name=_('joze 3'))
    joze4 = models.BooleanField(verbose_name=_('joze 4'))
    joze5 = models.BooleanField(verbose_name=_('joze 5'))
    joze6 = models.BooleanField(verbose_name=_('joze 6'))
    joze7 = models.BooleanField(verbose_name=_('joze 7'))
    joze8 = models.BooleanField(verbose_name=_('joze 8'))
    joze9 = models.BooleanField(verbose_name=_('joze 9'))
    joze10 = models.BooleanField(verbose_name=_('joze 10'))
    joze11 = models.BooleanField(verbose_name=_('joze 11'))
    joze12 = models.BooleanField(verbose_name=_('joze 12'))
    joze13 = models.BooleanField(verbose_name=_('joze 13'))
    joze14 = models.BooleanField(verbose_name=_('joze 14'))
    joze15 = models.BooleanField(verbose_name=_('joze 15'))
    joze16 = models.BooleanField(verbose_name=_('joze 16'))
    joze17 = models.BooleanField(verbose_name=_('joze 17'))
    joze18 = models.BooleanField(verbose_name=_('joze 18'))
    joze19 = models.BooleanField(verbose_name=_('joze 19'))
    joze20 = models.BooleanField(verbose_name=_('joze 20'))
    joze21 = models.BooleanField(verbose_name=_('joze 21'))
    joze22 = models.BooleanField(verbose_name=_('joze 22'))
    joze23 = models.BooleanField(verbose_name=_('joze 23'))
    joze24 = models.BooleanField(verbose_name=_('joze 24'))
    joze25 = models.BooleanField(verbose_name=_('joze 25'))
    joze26 = models.BooleanField(verbose_name=_('joze 26'))
    joze27 = models.BooleanField(verbose_name=_('joze 27'))
    joze28 = models.BooleanField(verbose_name=_('joze 28'))
    joze29 = models.BooleanField(verbose_name=_('joze 29'))
    joze30 = models.BooleanField(verbose_name=_('joze 30'))

    def __str__(self):
        return self.dead.fname + ' ' + self.dead.lname

    class Meta:
        verbose_name = _('Quran')
        verbose_name_plural = _('Quran')
