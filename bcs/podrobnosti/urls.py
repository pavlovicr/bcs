from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

#bcs
urlpatterns = [

    url(r'^dokumentacije/$', views.DokumentacijaList.as_view(), name='dokumentacija-list'),
    url(r'^dokumentacija/(?P<pk>\d+)$', views.DokumentacijaDetail.as_view(), name='dokumentacija-detail'),
    url(r'^slike/$', views.SlikaList.as_view(), name='slika-list'),
    url(r'^slika/(?P<pk>\d+)$', views.SlikaDetail.as_view(), name='slika-detail'),
    url(r'^datoteke/$', views.DatotekaList.as_view(), name='datoteka-list'),
    url(r'^datoteka/(?P<pk>\d+)$', views.DatotekaDetail.as_view(), name='datoteka-detail'),
    url(r'^predmeti/$', views.PredmetList.as_view(), name='predmet-list'),
    url(r'^predmet/(?P<pk>\d+)$', views.PredmetDetail.as_view(), name='predmet-detail'),
    url(r'^podlage/$', views.PodlagaList.as_view(), name='podlaga-list'),
    url(r'^podlaga/(?P<pk>\d+)$', views.PodlagaDetail.as_view(), name='podlaga-detail'),
    url(r'^merila/$', views.MeriloList.as_view(), name='merilo-list'),
    url(r'^merilo/(?P<pk>\d+)$', views.MeriloDetail.as_view(), name='merilo-detail'),
    url(r'^merila_osnova/$', views.MeriloOsnovaList.as_view(), name='meriloosnova-list'),
    url(r'^merilo_osnova/(?P<pk>\d+)$', views.MeriloOsnovaDetail.as_view(), name='meriloosnova-detail'),
    url(r'^merila_skupina1/$', views.MeriloSkupina1List.as_view(), name='meriloskupina1-list'),
    url(r'^merilo_skupina1/(?P<pk>\d+)$', views.MeriloSkupina1Detail.as_view(), name='meriloskupina1-detail'),
    url(r'^podrobnosti/$', views.PodrobnostList.as_view(), name='podrobnost-list'),
    url(r'^podrobnost/(?P<pk>\d+)$', views.PodrobnostDetail.as_view(), name='podrobnost-detail'),




]
