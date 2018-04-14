from django.shortcuts import render
from django.views import generic
from django.views.generic import DetailView
from django.views.generic import ListView
from django.shortcuts import get_object_or_404


from podrobnosti.models import Vir,Poglavje,Specifikacija,Odsek,Podrobnost,Gradivo,Namen


from django.http import HttpResponse
def specifikacija(request,tone='1'):
    a=Specifikacija.objects.get(pk=tone)
    return render(request, 'podrobnosti/specifikacija_detail.html',{'object':a})

from django.http import HttpResponseRedirect

from .forms import ImeForm

def get_ime(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ImeForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/podrobnosti/podrobnosti/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ImeForm()

    return render(request, 'podrobnosti/vaja.html', {'form': form})







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
        )
        return queryset


class SpecifikacijaDetail(DetailView):
    model = Specifikacija


class OdsekList(ListView):
    model = Odsek
#def get_queryset(self, *args, **kwargs):
#    queryset = super(SpecifikacijaList, self).get_queryset(*args, **kwargs)

#    queryset = queryset.order_by(
#        'tekst',
#            )
#    return queryset


class OdsekDetail(DetailView):
    model = Odsek


class PodrobnostList(ListView):
    model = Podrobnost

    def get_queryset(self, *args, **kwargs):
        queryset = super(PodrobnostList, self).get_queryset(*args, **kwargs)

        queryset = queryset.order_by(
            'specifikacija__dela__vrsta_del',
            'specifikacija__dela',
            'specifikacija__tip',
            'specifikacija__poglavje__stevilka', # vrstni red po številki poglavja
            'specifikacija__stevilka', # vrstni red po številki specifikacije
            'odsek',
            'stevilka',
            )
        return queryset


class PodrobnostDetail(DetailView):
    model = Podrobnost
