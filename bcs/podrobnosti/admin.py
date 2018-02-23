from django.contrib import admin

#bcs
from podrobnosti.models import Dokumentacija,PodlagaMerila,PredmetMerila,Merilo,Podrobnost,Slika,Datoteka



admin.site.register(Dokumentacija)
admin.site.register(PodlagaMerila)
admin.site.register(PredmetMerila)
admin.site.register(Merilo)
admin.site.register(Podrobnost)
admin.site.register(Slika)
admin.site.register(Datoteka)
