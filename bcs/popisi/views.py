from django.shortcuts import render
from django.views import generic
from django.views.generic import DetailView
from django.views.generic import ListView
from django.shortcuts import get_object_or_404

#bcs
from popisi.models import VrstaDel,Dela,Postavka,PopisnaPostavka,Podrobnost


class VrstaDelList(ListView):
    model = VrstaDel


class VrstaDelDetail(DetailView):
    model = VrstaDel


class DelaList(ListView):
    model = Dela


class DelaDetail(DetailView):
    model = Dela


class PostavkaList(ListView):
    model = Postavka


class PostavkaDetail(DetailView):
    model = Postavka


class PopisnaPostavkaList(ListView):
    model = PopisnaPostavka

    def get_queryset(self, *args, **kwargs):
        queryset = super(PopisnaPostavkaList, self).get_queryset(*args, **kwargs)

        queryset = queryset.order_by(
            'postavka',
        )
        return queryset




class PopisnaPostavkaDetail(DetailView):
    model = PopisnaPostavka
