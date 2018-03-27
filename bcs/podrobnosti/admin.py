from django.contrib import admin

#bcs
from podrobnosti.models import Vir,Specifikacija,Poglavje,Segment,Podrobnost,Gradivo,Namen



class GradivoInline(admin.StackedInline):
    model = Gradivo



class PodrobnostInline(admin.StackedInline):
    model = Podrobnost


class SpecifikacijaAdmin(admin.ModelAdmin):
    list_display = ['stevilka','tekst','podlaga']
    ordering = ['stevilka']

    inlines = [PodrobnostInline]


class VirAdmin(admin.ModelAdmin):
    list_display = ['stevilka','tekst']
    ordering = ['stevilka']

    inlines = [GradivoInline]

class PodrobnostAdmin(admin.ModelAdmin):
    read_only = ['gs']
    list_display = ['stevilka','tekst','gs']
    ordering = ['stevilka']







admin.site.register(Vir,VirAdmin)
admin.site.register(Specifikacija,SpecifikacijaAdmin)
admin.site.register(Poglavje)
admin.site.register(Segment)
admin.site.register(Podrobnost,PodrobnostAdmin)
admin.site.register(Gradivo)
admin.site.register(Namen)
