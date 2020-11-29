from django.db import models
from django.utils.translation import gettext_lazy as _

STATUS_CHOICES = (
    ('active', _('active')),
    ('inactive', _('inactive'))
)


class Deveased(models.Model):
    state = models.CharField(max_length=100, verbose_name=_('State'), null=True, blank=True)
    city = models.CharField(max_length=100, verbose_name=_('City'), null=True, blank=True)
    picture = models.ImageField(verbose_name=_('Picture'), null=True, blank=True)
    title = models.CharField(max_length=120, verbose_name=_('Title'), null=True, blank=True)
    fname = models.CharField(max_length=120, verbose_name=_('First Name'), null=True, blank=True)
    lname = models.CharField(max_length=120, verbose_name=_('Last Name'), null=True, blank=True)
    description = models.TextField(verbose_name=_('Description'), null=True, blank=True)
    address = models.TextField(verbose_name=_('Address'), null=True, blank=True)
    # quran = models.ForeignKey('Quran', on_delete=models.CASCADE, related_name='dead_quran', null=True)
    status = models.CharField(max_length=60, choices=STATUS_CHOICES, default='active', verbose_name=_('Status'))

    def __str__(self):
        return self.fname + " " + self.lname

    class Meta:
        verbose_name = _('Deveased')
        verbose_name_plural = _('Deveaseds')


class Fatehe(models.Model):
    fatehe = models.ForeignKey(Deveased, on_delete=models.CASCADE)
    status = models.CharField(max_length=60, choices=STATUS_CHOICES, default='active', verbose_name=_('Status'))

    def __str__(self):
        return self.fatehe.fname + ' '+ self.fatehe.lname


class Ashora(models.Model):
    ashora = models.ForeignKey(Deveased, on_delete=models.CASCADE)
    status = models.CharField(max_length=60, choices=STATUS_CHOICES, default='active', verbose_name=_('Status'))

    def __str__(self):
        return self.ashora.fname + ' '+ self.ashora.lname


class Arbain(models.Model):
    arbian = models.ForeignKey(Deveased, on_delete=models.CASCADE)
    status = models.CharField(max_length=60, choices=STATUS_CHOICES, default='active', verbose_name=_('Status'))

    def __str__(self):
        return self.arbian.fname + ' '+ self.arbian.lname


class Ahd(models.Model):
    ahd = models.ForeignKey(Deveased, on_delete=models.CASCADE)
    status = models.CharField(max_length=60, choices=STATUS_CHOICES, default='active', verbose_name=_('Status'))

    def __str__(self):
        return self.ahd.fname + ' '+ self.ahd.lname


class Aye(models.Model):
    aye = models.ForeignKey(Deveased, on_delete=models.CASCADE)
    status = models.CharField(max_length=60, choices=STATUS_CHOICES, default='active', verbose_name=_('Status'))

    def __str__(self):
        return self.aye.fname + ' '+ self.aye.lname


class Sahifeh(models.Model):
    sahifeh = models.ForeignKey(Deveased, on_delete=models.CASCADE)
    status = models.CharField(max_length=60, choices=STATUS_CHOICES, default='active', verbose_name=_('Status'))

    def __str__(self):
        return self.sahifeh.fname + ' '+ self.sahifeh.lname


class Komil(models.Model):
    komil = models.ForeignKey(Deveased, on_delete=models.CASCADE)
    status = models.CharField(max_length=60, choices=STATUS_CHOICES, default='active', verbose_name=_('Status'))

    def __str__(self):
        return self.komil.fname + ' '+ self.komil.lname


class Rabana(models.Model):
    rabana = models.ForeignKey(Deveased, on_delete=models.CASCADE)
    status = models.CharField(max_length=60, choices=STATUS_CHOICES, default='active', verbose_name=_('Status'))

    def __str__(self):
        return self.rabana.fname + ' '+ self.rabana.lname

    # joz_30 = models.ForeignKey('Quran', to_field='joze30', on_delete=models.CASCADE)


class Quran(models.Model):
    joze1 = models.BooleanField(verbose_name=_('joze 1'), default=False, null=True)
    joze2 = models.BooleanField(verbose_name=_('joze 2'), default=False, null=True)
    joze3 = models.BooleanField(verbose_name=_('joze 3'), default=False, null=True)
    joze4 = models.BooleanField(verbose_name=_('joze 4'), default=False, null=True)
    joze5 = models.BooleanField(verbose_name=_('joze 5'), default=False, null=True)
    joze6 = models.BooleanField(verbose_name=_('joze 6'), default=False, null=True)
    joze7 = models.BooleanField(verbose_name=_('joze 7'), default=False, null=True)
    joze8 = models.BooleanField(verbose_name=_('joze 8'), default=False, null=True)
    joze9 = models.BooleanField(verbose_name=_('joze 9'), default=False, null=True)
    joze10 = models.BooleanField(verbose_name=_('joze 10'), default=False, null=True)
    joze11 = models.BooleanField(verbose_name=_('joze 11'), default=False, null=True)
    joze12 = models.BooleanField(verbose_name=_('joze 12'), default=False, null=True)
    joze13 = models.BooleanField(verbose_name=_('joze 13'), default=False, null=True)
    joze14 = models.BooleanField(verbose_name=_('joze 14'), default=False, null=True)
    joze15 = models.BooleanField(verbose_name=_('joze 15'), default=False, null=True)
    joze16 = models.BooleanField(verbose_name=_('joze 16'), default=False, null=True)
    joze17 = models.BooleanField(verbose_name=_('joze 17'), default=False, null=True)
    joze18 = models.BooleanField(verbose_name=_('joze 18'), default=False, null=True)
    joze19 = models.BooleanField(verbose_name=_('joze 19'), default=False, null=True)
    joze20 = models.BooleanField(verbose_name=_('joze 20'), default=False, null=True)
    joze21 = models.BooleanField(verbose_name=_('joze 21'), default=False, null=True)
    joze22 = models.BooleanField(verbose_name=_('joze 22'), default=False, null=True)
    joze23 = models.BooleanField(verbose_name=_('joze 23'), default=False, null=True)
    joze24 = models.BooleanField(verbose_name=_('joze 24'), default=False, null=True)
    joze25 = models.BooleanField(verbose_name=_('joze 25'), default=False, null=True)
    joze26 = models.BooleanField(verbose_name=_('joze 26'), default=False, null=True)
    joze27 = models.BooleanField(verbose_name=_('joze 27'), default=False, null=True)
    joze28 = models.BooleanField(verbose_name=_('joze 28'), default=False, null=True)
    joze29 = models.BooleanField(verbose_name=_('joze 29'), default=False, null=True)
    joze30 = models.BooleanField(verbose_name=_('joze 30'), default=False, null=True)

    def __str__(self):
        return ' quran '
