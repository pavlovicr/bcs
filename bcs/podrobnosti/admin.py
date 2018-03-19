from django.contrib import admin

#bcs
from podrobnosti.models import Dokumentacija,Specifikacija,Poglavje,Segment,Podrobnost,Slika,Datoteka



admin.site.register(Dokumentacija)
admin.site.register(Specifikacija)
admin.site.register(Poglavje)
admin.site.register(Segment)
admin.site.register(Podrobnost)
admin.site.register(Slika)
admin.site.register(Datoteka)
