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
    url(r'^predmet_meril/$', views.PredmetMerilaList.as_view(), name='predmetmerila-list'),
    url(r'^predmet_merila/(?P<pk>\d+)$', views.PredmetMerilaDetail.as_view(), name='predmetmerila-detail'),
    url(r'^podlage_meril/$', views.PodlagaMerilaList.as_view(), name='podlagamerila-list'),
    url(r'^podlaga_merila/(?P<pk>\d+)$', views.PodlagaMerilaDetail.as_view(), name='podlagamerila-detail'),
    url(r'^merila/$', views.MeriloList.as_view(), name='merilo-list'),
    url(r'^merilo/(?P<pk>\d+)$', views.MeriloDetail.as_view(), name='merilo-detail'),
    url(r'^podrobnosti/$', views.PodrobnostList.as_view(), name='podrobnost-list'),
    url(r'^podrobnost/(?P<pk>\d+)$', views.PodrobnostDetail.as_view(), name='podrobnost-detail'),




]
