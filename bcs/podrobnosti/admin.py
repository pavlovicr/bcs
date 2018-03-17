from django.contrib import admin

#bcs
from podrobnosti.models import Dokumentacija,Specifikacija,Poglavje,Podskupina,Podrobnost,Slika,Datoteka



admin.site.register(Dokumentacija)
admin.site.register(Specifikacija)
admin.site.register(Poglavje)
admin.site.register(Podskupina)
admin.site.register(Podrobnost)
admin.site.register(Slika)
admin.site.register(Datoteka)
