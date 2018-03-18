from django.shortcuts import render
from django.views import generic
from django.views.generic import DetailView
from django.views.generic import ListView
from django.shortcuts import get_object_or_404

#bcs
from podrobnosti.models import Dokumentacija,Poglavje,Specifikacija,Podskupina,Podrobnost,Slika,Datoteka

class SlikaList(ListView):
    model = Slika


class SlikaDetail(DetailView):
    model = Slika


class DatotekaList(ListView):
    model = Datoteka


class DatotekaDetail(DetailView):
    model = Datoteka


class DokumentacijaList(ListView):
    model = Dokumentacija


class DokumentacijaDetail(DetailView):
    model = Dokumentacija


class PoglavjeList(ListView):
    model = Poglavje


class PoglavjeDetail(DetailView):
    model = Poglavje


class SpecifikacijaList(ListView):
    model = Specifikacija

    def get_queryset(self, *args, **kwargs):
        queryset = super(SpecifikacijaList, self).get_queryset(*args, **kwargs)

        queryset = queryset.order_by(
            'tip',
            'poglavje__dela__vrsta_del',
            'poglavje__dela',
            'poglavje',
            #'tekst'
        )
        return queryset


class SpecifikacijaDetail(DetailView):
    model = Specifikacija


class PodskupinaList(ListView):
    model = Podskupina


class PodskupinaDetail(DetailView):
    model = Podskupina


class PodrobnostList(ListView):
    model = Podrobnost


class PodrobnostDetail(DetailView):
    model = Podrobnost
