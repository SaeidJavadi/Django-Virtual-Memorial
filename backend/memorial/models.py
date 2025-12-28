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
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, verbose_name=_('State'),
                              related_name='citystate')
    city = models.CharField(max_length=120, verbose_name=_('City'))
    status = models.CharField(max_length=60, choices=STATUS_CHOICES, default='active', verbose_name=_('Status'))

    def __str__(self):
        return f"{self.city}"

    class Meta:
        verbose_name = _('City')
        verbose_name_plural = _('Citys')
        ordering = ('id',)
        unique_together = ('state', 'city')


class Deveased(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name=_('ID'), editable=True)
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, verbose_name=_('Phone'),
                             related_name='userdeads')
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, verbose_name=_('State'),
                              related_name='statedeads')
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, verbose_name=_('City'),
                             related_name='citydeads')
    picture = models.ImageField(verbose_name=_('Picture'), null=True, blank=True, upload_to='%Y-%m-%d', max_length=200)
    title = models.CharField(max_length=120, verbose_name=_('Title'), null=True, blank=True)
    name = models.CharField(max_length=120, verbose_name=_('Full Name'))
    gender = models.CharField(max_length=7, choices=(('male', _('Male')), ('female', _('Female'))), default='male',
                              verbose_name=_('Gender'))
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
    sahifeh_chk = models.BooleanField(verbose_name=_('Sahifeh'))
    komil_chk = models.BooleanField(verbose_name=_('Komil'))
    rahman_chk = models.BooleanField(verbose_name=_('Rahman'))
    yasin_chk = models.BooleanField(verbose_name=_('Yasin'))
    molk_chk = models.BooleanField(verbose_name=_('Molk'))
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


class Ziarat(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name=_('ID'), editable=True)
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, verbose_name=_('Phone'),
                             related_name='userziarat')
    state = models.ForeignKey(State, on_delete=models.CASCADE, verbose_name=_('State'), related_name='zstate')
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name=_('City'), related_name='cstate')
    description = models.TextField(verbose_name=_('Description'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('Created'))
    read = models.BooleanField(verbose_name=_('Read'), default=False)
    status = models.CharField(max_length=60, choices=STATUS_CHOICES, default='active', verbose_name=_('Status'))

    class Meta:
        verbose_name = _('Ziarat')
        verbose_name_plural = _('Ziarat')


class Fatehe(models.Model):
    dead = models.ForeignKey(Deveased, on_delete=models.CASCADE, verbose_name=_('Fatehe'), related_name='fdead')
    ip = models.CharField(max_length=20, verbose_name=_('ip'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.dead.id} - {self.dead.name}"

    class Meta:
        verbose_name = _('Fatehe')
        verbose_name_plural = _('Fatehe')


class Ashora(models.Model):
    dead = models.ForeignKey(Deveased, on_delete=models.CASCADE, verbose_name='Ashora', related_name='asdead')
    ip = models.CharField(max_length=20, verbose_name=_('ip'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.dead.id} - {self.dead.name}"

    class Meta:
        verbose_name = _('Ashora')
        verbose_name_plural = _('Ashora')


class Arbain(models.Model):
    dead = models.ForeignKey(Deveased, on_delete=models.CASCADE, verbose_name=_('Arbain'), related_name='ardead')
    ip = models.CharField(max_length=20, verbose_name=_('ip'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.dead.id} - {self.dead.name}"

    class Meta:
        verbose_name = _('Arbain')
        verbose_name_plural = _('Arbain')


class Ahd(models.Model):
    dead = models.ForeignKey(Deveased, on_delete=models.CASCADE, verbose_name=_('Ahd'), related_name='ahdead')
    ip = models.CharField(max_length=20, verbose_name=_('ip'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.dead.id} - {self.dead.name}"

    class Meta:
        verbose_name = _('Ahd')
        verbose_name_plural = _('Ahd')


class Aye(models.Model):
    dead = models.ForeignKey(Deveased, on_delete=models.CASCADE, verbose_name=_('Aye'), related_name='aydead')
    ip = models.CharField(max_length=20, verbose_name=_('ip'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.dead.id} - {self.dead.name}"

    class Meta:
        verbose_name = _('Aye')
        verbose_name_plural = _('Aye')


class Sahifeh(models.Model):
    dead = models.ForeignKey(Deveased, on_delete=models.CASCADE, verbose_name=_('Sahifeh'), related_name='sadead')
    ip = models.CharField(max_length=20, verbose_name=_('ip'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.dead.id} - {self.dead.name}"

    class Meta:
        verbose_name = _('Sahifeh')
        verbose_name_plural = _('Sahifeh')


class Komil(models.Model):
    dead = models.ForeignKey(Deveased, on_delete=models.CASCADE, verbose_name=_('Komil'), related_name='kdead')
    ip = models.CharField(max_length=20, verbose_name=_('ip'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.dead.id} - {self.dead.name}"

    class Meta:
        verbose_name = _('Komil')
        verbose_name_plural = _('Komil')


class Rahman(models.Model):
    dead = models.ForeignKey(Deveased, on_delete=models.CASCADE, verbose_name=_('Rahman'), related_name='rdead')
    ip = models.CharField(max_length=20, verbose_name=_('ip'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.dead.id} - {self.dead.name}"

    class Meta:
        verbose_name = _('Rahman')
        verbose_name_plural = _('Rahman')


class Yasin(models.Model):
    dead = models.ForeignKey(Deveased, on_delete=models.CASCADE, verbose_name=_('Yasin'), related_name='yadead')
    ip = models.CharField(max_length=20, verbose_name=_('ip'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.dead.id} - {self.dead.name}"

    class Meta:
        verbose_name = _('Yasin')
        verbose_name_plural = _('Yasin')


class Molk(models.Model):
    dead = models.ForeignKey(Deveased, on_delete=models.CASCADE, verbose_name=_('Molk'), related_name='modead')
    ip = models.CharField(max_length=20, verbose_name=_('ip'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.dead.id} - {self.dead.name}"

    class Meta:
        verbose_name = _('Molk')
        verbose_name_plural = _('Molk')


class Salavat(models.Model):
    dead = models.ForeignKey(Deveased, on_delete=models.CASCADE, verbose_name=_('Salavat'), related_name='sdead')
    ip = models.CharField(max_length=20, verbose_name=_('ip'), null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.dead.id} - {self.dead.name}"

    class Meta:
        verbose_name = _('Salavat')
        verbose_name_plural = _('Salavat')


class Quran(models.Model):
    dead = models.OneToOneField(Deveased, on_delete=models.CASCADE, verbose_name=_('Dead'), related_name='deadquran',
                                unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.dead.id} - {self.dead.name}"

    class Meta:
        verbose_name = _('Quran')
        verbose_name_plural = _('Quran')


class Joz1(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'), related_name='j1')
    ip = models.CharField(max_length=20, verbose_name=_('ip'), null=True, blank=True)

    def __str__(self):
        return f"{self.quran.dead.id}-{self.quran.dead.name}"


class Joz2(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'), related_name='j2')
    ip = models.CharField(max_length=20, verbose_name=_('ip'), null=True, blank=True)

    def __str__(self):
        return f"{self.quran.dead.id}-{self.quran.dead.name}"


class Joz3(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'), related_name='j3')
    ip = models.CharField(max_length=20, verbose_name=_('ip'), null=True, blank=True)

    def __str__(self):
        return f"{self.quran.dead.id}-{self.quran.dead.name}"


class Joz4(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'), related_name='j4')
    ip = models.CharField(max_length=20, verbose_name=_('ip'), null=True, blank=True)

    def __str__(self):
        return f"{self.quran.dead.id}-{self.quran.dead.name}"


class Joz5(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'), related_name='j5')
    ip = models.CharField(max_length=20, verbose_name=_('ip'), null=True, blank=True)

    def __str__(self):
        return f"{self.quran.dead.id}-{self.quran.dead.name}"


class Joz6(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'), related_name='j6')
    ip = models.CharField(max_length=20, verbose_name=_('ip'), null=True, blank=True)

    def __str__(self):
        return f"{self.quran.dead.id}-{self.quran.dead.name}"


class Joz7(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'), related_name='j7')
    ip = models.CharField(max_length=20, verbose_name=_('ip'), null=True, blank=True)

    def __str__(self):
        return f"{self.quran.dead.id}-{self.quran.dead.name}"


class Joz8(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'), related_name='j8')
    ip = models.CharField(max_length=20, verbose_name=_('ip'), null=True, blank=True)

    def __str__(self):
        return f"{self.quran.dead.id}-{self.quran.dead.name}"


class Joz9(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'), related_name='j9')
    ip = models.CharField(max_length=20, verbose_name=_('ip'), null=True, blank=True)

    def __str__(self):
        return f"{self.quran.dead.id}-{self.quran.dead.name}"


class Joz10(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'), related_name='j10')
    ip = models.CharField(max_length=20, verbose_name=_('ip'), null=True, blank=True)

    def __str__(self):
        return f"{self.quran.dead.id}-{self.quran.dead.name}"


class Joz11(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'), related_name='j11')
    ip = models.CharField(max_length=20, verbose_name=_('ip'), null=True, blank=True)

    def __str__(self):
        return f"{self.quran.dead.id}-{self.quran.dead.name}"


class Joz12(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'), related_name='j12')
    ip = models.CharField(max_length=20, verbose_name=_('ip'), null=True, blank=True)

    def __str__(self):
        return f"{self.quran.dead.id}-{self.quran.dead.name}"


class Joz13(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'), related_name='j13')
    ip = models.CharField(max_length=20, verbose_name=_('ip'), null=True, blank=True)

    def __str__(self):
        return f"{self.quran.dead.id}-{self.quran.dead.name}"


class Joz14(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'), related_name='j14')
    ip = models.CharField(max_length=20, verbose_name=_('ip'), null=True, blank=True)

    def __str__(self):
        return f"{self.quran.dead.id}-{self.quran.dead.name}"


class Joz15(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'), related_name='j15')
    ip = models.CharField(max_length=20, verbose_name=_('ip'), null=True, blank=True)

    def __str__(self):
        return f"{self.quran.dead.id}-{self.quran.dead.name}"


class Joz16(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'), related_name='j16')
    ip = models.CharField(max_length=20, verbose_name=_('ip'), null=True, blank=True)

    def __str__(self):
        return f"{self.quran.dead.id}-{self.quran.dead.name}"


class Joz17(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'), related_name='j17')
    ip = models.CharField(max_length=20, verbose_name=_('ip'), null=True, blank=True)

    def __str__(self):
        return f"{self.quran.dead.id}-{self.quran.dead.name}"


class Joz18(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'), related_name='j18')
    ip = models.CharField(max_length=20, verbose_name=_('ip'), null=True, blank=True)

    def __str__(self):
        return f"{self.quran.dead.id}-{self.quran.dead.name}"


class Joz19(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'), related_name='j19')
    ip = models.CharField(max_length=20, verbose_name=_('ip'), null=True, blank=True)

    def __str__(self):
        return f"{self.quran.dead.id}-{self.quran.dead.name}"


class Joz20(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'), related_name='j20')
    ip = models.CharField(max_length=20, verbose_name=_('ip'), null=True, blank=True)

    def __str__(self):
        return f"{self.quran.dead.id}-{self.quran.dead.name}"


class Joz21(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'), related_name='j21')
    ip = models.CharField(max_length=20, verbose_name=_('ip'), null=True, blank=True)

    def __str__(self):
        return f"{self.quran.dead.id}-{self.quran.dead.name}"


class Joz22(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'), related_name='j22')
    ip = models.CharField(max_length=20, verbose_name=_('ip'), null=True, blank=True)

    def __str__(self):
        return f"{self.quran.dead.id}-{self.quran.dead.name}"


class Joz23(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'), related_name='j23')
    ip = models.CharField(max_length=20, verbose_name=_('ip'), null=True, blank=True)

    def __str__(self):
        return f"{self.quran.dead.id}-{self.quran.dead.name}"


class Joz24(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'), related_name='j24')
    ip = models.CharField(max_length=20, verbose_name=_('ip'), null=True, blank=True)

    def __str__(self):
        return f"{self.quran.dead.id}-{self.quran.dead.name}"


class Joz25(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'), related_name='j25')
    ip = models.CharField(max_length=20, verbose_name=_('ip'), null=True, blank=True)

    def __str__(self):
        return f"{self.quran.dead.id}-{self.quran.dead.name}"


class Joz26(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'), related_name='j26')
    ip = models.CharField(max_length=20, verbose_name=_('ip'), null=True, blank=True)

    def __str__(self):
        return f"{self.quran.dead.id}-{self.quran.dead.name}"


class Joz27(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'), related_name='j27')
    ip = models.CharField(max_length=20, verbose_name=_('ip'), null=True, blank=True)

    def __str__(self):
        return f"{self.quran.dead.id}-{self.quran.dead.name}"


class Joz28(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'), related_name='j28')
    ip = models.CharField(max_length=20, verbose_name=_('ip'), null=True, blank=True)

    def __str__(self):
        return f"{self.quran.dead.id}-{self.quran.dead.name}"


class Joz29(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'), related_name='j29')
    ip = models.CharField(max_length=20, verbose_name=_('ip'), null=True, blank=True)

    def __str__(self):
        return f"{self.quran.dead.id}-{self.quran.dead.name}"


class Joz30(models.Model):
    quran = models.ForeignKey(Quran, on_delete=models.CASCADE, verbose_name=_('Quran'), related_name='j30')
    ip = models.CharField(max_length=20, verbose_name=_('ip'), null=True, blank=True)

    def __str__(self):
        return f"{self.quran.dead.id}-{self.quran.dead.name}"
