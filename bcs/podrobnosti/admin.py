from django.contrib import admin

#bcs
from podrobnosti.models import Vir,Specifikacija,Poglavje,Odsek,Podrobnost,Gradivo,Namen



class GradivoInline(admin.StackedInline):
    model = Gradivo
    extra=1


class PodrobnostInline(admin.StackedInline):
    model = Podrobnost
    extra=1

class SpecifikacijaAdmin(admin.ModelAdmin):
    list_display = ['tekst','tekst_za_popis','tip','poglavje','podlaga','dela']
    list_filter = ('tip', 'poglavje')
    ordering = ['tip','poglavje__stevilka','stevilka']
    exclude = ('stevilka',)
    inlines = [PodrobnostInline]


class VirAdmin(admin.ModelAdmin):
    list_display = ['stevilka','tekst']
    ordering = ['stevilka']

    inlines = [GradivoInline]


class PodrobnostAdmin(admin.ModelAdmin):
    #read_only = ['gs']
    list_display = ['stevilka','tekst','tekst_za_popis','specifikacija']
    list_filter = ('specifikacija__tip', 'specifikacija__poglavje')
    ordering = ['specifikacija__tip','specifikacija__stevilka','stevilka']


class OdsekAdmin(admin.ModelAdmin):
    list_display = ['stevilka','tekst','tekst_za_popis']
    ordering = ['stevilka']

    inlines = [PodrobnostInline]

admin.site.register(Vir,VirAdmin)
admin.site.register(Specifikacija,SpecifikacijaAdmin)
admin.site.register(Poglavje)
admin.site.register(Odsek,OdsekAdmin)
admin.site.register(Podrobnost,PodrobnostAdmin)
admin.site.register(Gradivo)
admin.site.register(Namen)
