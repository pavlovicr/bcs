from django.shortcuts import render
from django.views import generic
from django.views.generic import DetailView
from django.views.generic import ListView
from django.shortcuts import get_object_or_404

#bcs
from podrobnosti.models import Dokumentacija,Predmet,Podlaga,Merilo,MeriloOsnova,MeriloSkupina1,Podrobnost,Slika,Datoteka


class DokumentacijaList(ListView):
    model = Dokumentacija


class DokumentacijaDetail(DetailView):
    model = Dokumentacija


class SlikaList(ListView):
    model = Slika


class SlikaDetail(DetailView):
    model = Slika


class DatotekaList(ListView):
    model = Datoteka


class DatotekaDetail(DetailView):
    model = Datoteka


class PredmetList(ListView):
    model = Predmet


class PredmetDetail(DetailView):
    model = Predmet


class PodlagaList(ListView):
    model = Podlaga


class PodlagaDetail(DetailView):
    model = Podlaga

class MeriloList(ListView):
    model = Merilo


class MeriloDetail(DetailView):
    model = Merilo


class MeriloOsnovaList(ListView):
    model = MeriloOsnova


class MeriloOsnovaDetail(DetailView):
    model = MeriloOsnova


class MeriloSkupina1List(ListView):
    model = MeriloSkupina1


class MeriloSkupina1Detail(DetailView):
    model = MeriloSkupina1


class PodrobnostList(ListView):
    model = Podrobnost

    def get_queryset(self):
        return Podrobnost.objects.order_by('-opis')


class PodrobnostDetail(DetailView):
    model = Podrobnost
