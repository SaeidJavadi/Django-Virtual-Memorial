from django.contrib import admin
from memorial.models import *


@admin.register(Deveased)
class DeveasedAdmin(admin.ModelAdmin):
    list_display = ('fname', 'lname')

@admin.register(Quran)
class QuranAdmin(admin.ModelAdmin):
    list_display = ('joze1',)

@admin.register(Fatehe)
class FateheAdmin(admin.ModelAdmin):
    pass

@admin.register(Ashora)
class AshoraAdmin(admin.ModelAdmin):
    pass

@admin.register(Arbain)
class ArbainAdmin(admin.ModelAdmin):
    pass

@admin.register(Ahd)
class AhdAdmin(admin.ModelAdmin):
    pass

@admin.register(Aye)
class AyeAdmin(admin.ModelAdmin):
    pass

@admin.register(Sahifeh)
class SahifehAdmin(admin.ModelAdmin):
    pass

@admin.register(Komil)
class KomilhAdmin(admin.ModelAdmin):
    pass

@admin.register(Rabana)
class RabanahAdmin(admin.ModelAdmin):
    pass


