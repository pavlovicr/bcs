from django.contrib import admin

#bcs
from popisi.models import Dela,Postavka,VrstaDel,PopisnaPostavka

class PopisnaPostavkaAdmin(admin.ModelAdmin):
    list_display = ['stevilka','tekst']
    ordering = ['stevilka']


admin.site.register(Dela)
admin.site.register(Postavka,PopisnaPostavkaAdmin)
admin.site.register(VrstaDel)
admin.site.register(PopisnaPostavka)
