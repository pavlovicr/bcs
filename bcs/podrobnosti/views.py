from django.shortcuts import render
from django.views import generic
from django.views.generic import DetailView
from django.views.generic import ListView
from django.shortcuts import get_object_or_404

#bcs
from podrobnosti.models import Vir,Poglavje,Specifikacija,Podrobnost2,Podrobnost1,Gradivo,Namen

#def stev(request):
#    stevilka = Podrobnost.objects.all()
#    return render(request,'podrobnost.stev.html',
#            context={'':stevilka}
#    )
def stev(request):
    a=Podrobnost.objects.all()
    return render(request,'podrobnosti/stev.html',
     context={'b':a},
     )



class NamenList(ListView):
    model = Namen


class NamenDetail(DetailView):
    model = Namen


class GradivoList(ListView):
    model = Gradivo


class GradivoDetail(DetailView):
    model = Gradivo


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
            'dela__vrsta_del',
            'dela',
            'poglavje',
            'stevilka',
            #'tekst'
        )
        return queryset


class SpecifikacijaDetail(DetailView):
    model = Specifikacija


class Podrobnost1List(ListView):
    model = Podrobnost1

#    def get_queryset(self, *args, **kwargs):
#        queryset = super(SpecifikacijaList, self).get_queryset(*args, **kwargs)

#        queryset = queryset.order_by(
#            'specifikacija__stevilka',
#        )
#        return queryset


class Podrobnost1Detail(DetailView):
    model = Podrobnost1


class Podrobnost2List(ListView):
    model = Podrobnost2


class Podrobnost2Detail(DetailView):
    model = Podrobnost2
