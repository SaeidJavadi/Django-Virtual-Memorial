from django.contrib import admin
from memorial.models import *


@admin.register(Deveased)
class DeveasedAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user', 'created', 'updated', 'status')
    list_editable = ('status',)
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')


@admin.register(Quran)
class QuranAdmin(admin.ModelAdmin):
    list_display = ('dead',)


@admin.register(Fatehe)
class FateheAdmin(admin.ModelAdmin):
    list_display = ('ip', 'dead', 'created')

@admin.register(Salavat)
class SalavatAdmin(admin.ModelAdmin):
    list_display = ('ip', 'dead', 'created')


@admin.register(Ashora)
class AshoraAdmin(admin.ModelAdmin):
    list_display = ('ip', 'dead', 'created')


@admin.register(Arbain)
class ArbainAdmin(admin.ModelAdmin):
    list_display = ('ip', 'dead', 'created')

#
# @admin.register(Ahd)
# class AhdAdmin(admin.ModelAdmin):
#     list_display = ('ip', 'dead', 'created')
#
#
# @admin.register(Aye)
# class AyeAdmin(admin.ModelAdmin):
#     list_display = ('ip', 'dead', 'created')
#
#
# @admin.register(Sahifeh)
# class SahifehAdmin(admin.ModelAdmin):
#     list_display = ('ip', 'dead', 'created')
#
#
# @admin.register(Komil)
# class KomilhAdmin(admin.ModelAdmin):
#     list_display = ('ip', 'dead', 'created')
#
#
# @admin.register(Rahman)
# class RahmanhAdmin(admin.ModelAdmin):
#     list_display = ('ip', 'dead', 'created')
#

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('id', 'state', 'status')
    list_editable = ('status',)
    search_fields = ('id', 'state')


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'state', 'city', 'status')
    list_editable = ('status',)
    search_fields = ('id', 'state', 'city')


