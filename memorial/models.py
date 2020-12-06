from django.db import models
from django.utils.translation import gettext_lazy as _

STATUS_CHOICES = (
    ('active', _('active')),
    ('inactive', _('inactive'))
)


class State(models.Model):
    state = models.CharField(max_length=120, verbose_name=_('State'))
    status = models.CharField(max_length=60, choices=STATUS_CHOICES, default='active', verbose_name=_('Status'))

    def __str__(self):
        return self.state

    class Meta:
        verbose_name = _('State')
        verbose_name_plural = _('States')


class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, verbose_name=_('State'))
    city = models.CharField(max_length=120, verbose_name=_('City'))
    status = models.CharField(max_length=60, choices=STATUS_CHOICES, default='active', verbose_name=_('Status'))

    def __str__(self):
        return f"{self.state} '-' {self.city}"

    class Meta:
        verbose_name = _('City')
        verbose_name_plural = _('Citys')


class Deveased(models.Model):
    user_phone = models.ForeignKey('accounts.User', on_delete=models.CASCADE, verbose_name=_('Phone'))
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True ,verbose_name=_('City'))
    picture = models.ImageField(verbose_name=_('Picture'), null=True, blank=True)
    title = models.CharField(max_length=120, verbose_name=_('Title'), null=True, blank=True)
    fname = models.CharField(max_length=120, verbose_name=_('First Name'), null=True, blank=True)
    lname = models.CharField(max_length=120, verbose_name=_('Last Name'), null=True, blank=True)
    description = models.TextField(verbose_name=_('Description'), null=True, blank=True)
    address = models.TextField(verbose_name=_('Address'), null=True, blank=True)
    quran_chk = models.BooleanField(verbose_name=_('Quran'))
    fatehe_chk = models.BooleanField(verbose_name=_('Fatehe'))
    ashora_chk = models.BooleanField(verbose_name=_('Ashora'))
    arbain_chk = models.BooleanField(verbose_name=_('Arbain'))
    ahd_chk = models.BooleanField(verbose_name=_('Ahd'))
    aye_chk = models.BooleanField(verbose_name=_('Aye'))
    Sahifeh_chk = models.BooleanField(verbose_name=_('Sahifeh'))
    komil_chk = models.BooleanField(verbose_name=_('Komil'))
    rabana_chk = models.BooleanField(verbose_name=_('Rabana'))
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=60, choices=STATUS_CHOICES, default='active', verbose_name=_('Status'))

    def __str__(self):
        return self.fname + " " + self.lname

    class Meta:
        verbose_name = _('Deveased')
        verbose_name_plural = _('Deveaseds')


class Fatehe(models.Model):
    fatehe = models.ForeignKey(Deveased, on_delete=models.CASCADE, verbose_name=_('Fatehe'))
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
    arbain = models.ForeignKey(Deveased, on_delete=models.CASCADE, verbose_name=_('Arbain'))
    ip = models.CharField(max_length=20, verbose_name=_('ip'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.arbian.fname + ' ' + self.arbian.lname

    class Meta:
        verbose_name = _('Arbain')
        verbose_name_plural = _('Arbain')


class Ahd(models.Model):
    ahd = models.ForeignKey(Deveased, on_delete=models.CASCADE, verbose_name=_('Ahd'))
    ip = models.CharField(max_length=20, verbose_name=_('ip'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ahd.fname + ' ' + self.ahd.lname

    class Meta:
        verbose_name = _('Ahd')
        verbose_name_plural = _('Ahd')


class Aye(models.Model):
    aye = models.ForeignKey(Deveased, on_delete=models.CASCADE, verbose_name=_('Aye'))
    ip = models.CharField(max_length=20, verbose_name=_('ip'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.aye.fname + ' ' + self.aye.lname

    class Meta:
        verbose_name = _('Aye')
        verbose_name_plural = _('Aye')


class Sahifeh(models.Model):
    Sahifeh = models.ForeignKey(Deveased, on_delete=models.CASCADE, verbose_name=_('Sahifeh'))
    ip = models.CharField(max_length=20, verbose_name=_('ip'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Sahifeh.fname + ' ' + self.Sahifeh.lname

    class Meta:
        verbose_name = _('Sahifeh')
        verbose_name_plural = _('Sahifeh')


class Komil(models.Model):
    komil = models.ForeignKey(Deveased, on_delete=models.CASCADE, verbose_name=_('Komil'))
    ip = models.CharField(max_length=20, verbose_name=_('ip'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.komil.fname + ' ' + self.komil.lname

    class Meta:
        verbose_name = _('Komil')
        verbose_name_plural = _('Komil')


class Rabana(models.Model):
    rabana = models.ForeignKey(Deveased, on_delete=models.CASCADE, verbose_name=_('Rabana'))
    ip = models.CharField(max_length=20, verbose_name=_('ip'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.rabana.fname + ' ' + self.rabana.lname

    class Meta:
        verbose_name = _('Rabana')
        verbose_name_plural = _('Rabana')


class Salavat(models.Model):
    salavat = models.ForeignKey(Deveased, on_delete=models.CASCADE, verbose_name=_('Salavat'))
    ip = models.CharField(max_length=20, verbose_name=_('ip'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.salavat.fname + ' ' + self.salavat.lname

    class Meta:
        verbose_name = _('Salavat')
        verbose_name_plural = _('Salavat')


class Quran(models.Model):
    dead = models.ForeignKey(Deveased, on_delete=models.CASCADE, verbose_name=_('Dead'))
    status = models.CharField(max_length=60, choices=STATUS_CHOICES, default='active', verbose_name=_('Status'))

    def __str__(self):
        return self.dead.fname + ' ' + self.dead.lname

    class Meta:
        verbose_name = _('Quran')
        verbose_name_plural = _('Quran')


class Joz1(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'))

    def __str__(self):
        return self.quran.dead.fname + ' ' + self.quran.dead.lname


class Joze2(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'))

    def __str__(self):
        return self.quran.dead.fname + ' ' + self.quran.dead.lname


class Joze3(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'))

    def __str__(self):
        return self.quran.dead.fname + ' ' + self.quran.dead.lname


class Joze4(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'))

    def __str__(self):
        return self.quran.dead.fname + ' ' + self.quran.dead.lname


class Joze5(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'))

    def __str__(self):
        return self.quran.dead.fname + ' ' + self.quran.dead.lname


class Joze6(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'))

    def __str__(self):
        return self.quran.dead.fname + ' ' + self.quran.dead.lname


class Joze7(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'))

    def __str__(self):
        return self.quran.dead.fname + ' ' + self.quran.dead.lname


class Joze8(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'))

    def __str__(self):
        return self.quran.dead.fname + ' ' + self.quran.dead.lname


class Joze9(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'))

    def __str__(self):
        return self.quran.dead.fname + ' ' + self.quran.dead.lname


class Joze10(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'))

    def __str__(self):
        return self.quran.dead.fname + ' ' + self.quran.dead.lname


class Joze11(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'))

    def __str__(self):
        return self.quran.dead.fname + ' ' + self.quran.dead.lname


class Joze12(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'))

    def __str__(self):
        return self.quran.dead.fname + ' ' + self.quran.dead.lname


class Joze13(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'))

    def __str__(self):
        return self.quran.dead.fname + ' ' + self.quran.dead.lname


class Joze14(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'))

    def __str__(self):
        return self.quran.dead.fname + ' ' + self.quran.dead.lname


class Joze15(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'))

    def __str__(self):
        return self.quran.dead.fname + ' ' + self.quran.dead.lname


class Joze16(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'))

    def __str__(self):
        return self.quran.dead.fname + ' ' + self.quran.dead.lname


class Joze17(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'))

    def __str__(self):
        return self.quran.dead.fname + ' ' + self.quran.dead.lname


class Joze18(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'))

    def __str__(self):
        return self.quran.dead.fname + ' ' + self.quran.dead.lname


class Joze19(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'))

    def __str__(self):
        return self.quran.dead.fname + ' ' + self.quran.dead.lname


class Joze20(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'))

    def __str__(self):
        return self.quran.dead.fname + ' ' + self.quran.dead.lname


class Joze21(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'))

    def __str__(self):
        return self.quran.dead.fname + ' ' + self.quran.dead.lname


class Joze22(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'))

    def __str__(self):
        return self.quran.dead.fname + ' ' + self.quran.dead.lname


class Joze23(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'))

    def __str__(self):
        return self.quran.dead.fname + ' ' + self.quran.dead.lname


class Joze24(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'))

    def __str__(self):
        return self.quran.dead.fname + ' ' + self.quran.dead.lname


class Joze25(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'))

    def __str__(self):
        return self.quran.dead.fname + ' ' + self.quran.dead.lname


class Joze26(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'))

    def __str__(self):
        return self.quran.dead.fname + ' ' + self.quran.dead.lname


class Joze27(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'))

    def __str__(self):
        return self.quran.dead.fname + ' ' + self.quran.dead.lname


class Joze28(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'))

    def __str__(self):
        return self.quran.dead.fname + ' ' + self.quran.dead.lname


class Joze29(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'))

    def __str__(self):
        return self.quran.dead.fname + ' ' + self.quran.dead.lname


class Joze30(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'))

    def __str__(self):
        return self.quran.dead.fname + ' ' + self.quran.dead.lname
