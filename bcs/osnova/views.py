from django.shortcuts import render
from django.views import generic
from django.views.generic import DetailView
from django.views.generic import ListView
from django.shortcuts import get_object_or_404

from popisi.models import VrstaDel,Dela,Postavka
from podrobnosti.models import Podrobnost1,Specifikacija

def index(request):

    stej_specifikacija = Specifikacija.objects.all().count()
    stej_postavka = Postavka.objects.all().count()
    stej_dela = Dela.objects.all().count()
    stej_vrstadel = VrstaDel.objects.all().count()

    return render(request,'osnova/index.html',
     context={'stej_specifikacija':stej_specifikacija,'stej_postavka':stej_postavka,'stej_dela':stej_dela,'stej_vrstadel':stej_vrstadel,},
     )
