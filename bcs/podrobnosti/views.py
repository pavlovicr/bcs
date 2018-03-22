from django.shortcuts import render
from django.views import generic
from django.views.generic import DetailView
from django.views.generic import ListView
from django.shortcuts import get_object_or_404

#bcs
from podrobnosti.models import Vir,Poglavje,Specifikacija,Segment,Podrobnost,Slika,Datoteka

class SlikaList(ListView):
    model = Slika


class SlikaDetail(DetailView):
    model = Slika


class DatotekaList(ListView):
    model = Datoteka


class DatotekaDetail(DetailView):
    model = Datoteka


class VirList(ListView):
    model = Vir


class VirDetail(DetailView):
    model = Vir


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
            'stevilka',
            #'tekst'
        )
        return queryset


class SpecifikacijaDetail(DetailView):
    model = Specifikacija


class SegmentList(ListView):
    model = Segment


class SegmentDetail(DetailView):
    model = Segment


class PodrobnostList(ListView):
    model = Podrobnost


class PodrobnostDetail(DetailView):
    model = Podrobnost
