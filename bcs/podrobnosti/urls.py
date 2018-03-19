from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

#bcs
urlpatterns = [

    url(r'^slike/$', views.SlikaList.as_view(), name='slika-list'),
    url(r'^slika/(?P<pk>\d+)$', views.SlikaDetail.as_view(), name='slika-detail'),
    url(r'^datoteke/$', views.DatotekaList.as_view(), name='datoteka-list'),
    url(r'^datoteka/(?P<pk>\d+)$', views.DatotekaDetail.as_view(), name='datoteka-detail'),
    url(r'^dokumentacije/$', views.DokumentacijaList.as_view(), name='dokumentacija-list'),
    url(r'^dokumentacija/(?P<pk>\d+)$', views.DokumentacijaDetail.as_view(), name='dokumentacija-detail'),
    url(r'^poglavja/$', views.PoglavjeList.as_view(), name='poglavje-list'),
    url(r'^poglavje/(?P<pk>\d+)$', views.PoglavjeDetail.as_view(), name='poglavje-detail'),
    url(r'^specifikacije/$', views.SpecifikacijaList.as_view(), name='specifikacija-list'),
    url(r'^specifikacija/(?P<pk>\d+)$', views.SpecifikacijaDetail.as_view(), name='specifikacija-detail'),
    url(r'^segmenti/$', views.SegmentList.as_view(), name='segment-list'),
    url(r'^segment/(?P<pk>\d+)$', views.SegmentDetail.as_view(), name='segment-detail'),
    url(r'^podrobnosti/$', views.PodrobnostList.as_view(), name='podrobnost-list'),
    url(r'^podrobnost/(?P<pk>\d+)$', views.PodrobnostDetail.as_view(), name='podrobnost-detail'),


]
