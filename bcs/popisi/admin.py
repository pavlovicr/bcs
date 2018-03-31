from django.contrib import admin

#bcs
from popisi.models import Dela,Postavka,VrstaDel,PopisnaPostavka

class PopisnaPostavkaAdmin(admin.ModelAdmin):
    list_display = ['stevilka','tekst','hec']
    ordering = ['stevilka']


admin.site.register(Dela)
admin.site.register(Postavka)
admin.site.register(VrstaDel)
admin.site.register(PopisnaPostavka,PopisnaPostavkaAdmin)
