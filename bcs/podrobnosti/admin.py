from django.contrib import admin

#bcs
from podrobnosti.models import Vir,Specifikacija,Poglavje,Podrobnost2,Podrobnost1,Gradivo,Namen


class GradivoInline(admin.StackedInline):
    model = Gradivo
    extra=1


class Podrobnost1Inline(admin.StackedInline):
    model = Podrobnost1
    extra=1

class Podrobnost2Inline(admin.StackedInline):
    model = Podrobnost2
    extra=1


class SpecifikacijaAdmin(admin.ModelAdmin):
    list_display = ['stevilka','tekst','tip','poglavje','podlaga','dela']
    list_filter = ('tip', 'poglavje')
    ordering = ['tip','poglavje__stevilka','stevilka']
    inlines = [Podrobnost1Inline]


class VirAdmin(admin.ModelAdmin):
    list_display = ['stevilka','tekst']
    ordering = ['stevilka']

    inlines = [GradivoInline]


class Podrobnost1Admin(admin.ModelAdmin):
    #read_only = ['gs']
    list_display = ['stevilka','tekst','vaja','gs']
    list_filter = ('specifikacija__tip', 'specifikacija__poglavje')
    ordering = ['specifikacija__tip','specifikacija__stevilka']

    inlines = [Podrobnost2Inline]


class Podrobnost2Admin(admin.ModelAdmin):
    list_display = ['stevilka','tekst']
    ordering = ['podrobnost1__specifikacija__tip','podrobnost1__specifikacija__stevilka']


admin.site.register(Vir,VirAdmin)
admin.site.register(Specifikacija,SpecifikacijaAdmin)
admin.site.register(Poglavje)
admin.site.register(Podrobnost2,Podrobnost2Admin)
admin.site.register(Podrobnost1,Podrobnost1Admin)
admin.site.register(Gradivo)
admin.site.register(Namen)
