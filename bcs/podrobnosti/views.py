from django.shortcuts import render
from django.views import generic
from django.views.generic import DetailView
from django.views.generic import ListView
from django.shortcuts import get_object_or_404

#bcs
from podrobnosti.models import Dokumentacija,PredmetMerila,PodlagaMerila,Merilo,Podrobnost,Slika,Datoteka


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


class PredmetMerilaList(ListView):
    model = PredmetMerila


class PredmetMerilaDetail(DetailView):
    model = PredmetMerila


class PodlagaMerilaList(ListView):
    model = PodlagaMerila


class PodlagaMerilaDetail(DetailView):
    model = PodlagaMerila


class MeriloList(ListView):
    model = Merilo


class MeriloDetail(DetailView):
    model = Merilo


class PodrobnostList(ListView):
    model = Podrobnost


class PodrobnostDetail(DetailView):
    model = Podrobnost


class PodrobnostDetail(DetailView):
    model = Podrobnost
