from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

#bcs
urlpatterns = [
    url(r'^$', views.stev, name='stev'),

    url(r'^nameni/$', views.NamenList.as_view(), name='namen-list'),
    url(r'^namen/(?P<pk>\d+)$', views.NamenDetail.as_view(), name='namen-detail'),
    url(r'^gradiva/$', views.GradivoList.as_view(), name='gradivo-list'),
    url(r'^gradivo/(?P<pk>\d+)$', views.GradivoDetail.as_view(), name='gradivo-detail'),
    url(r'^viri/$', views.VirList.as_view(), name='vir-list'),
    url(r'^vir/(?P<pk>\d+)$', views.VirDetail.as_view(), name='vir-detail'),
    url(r'^poglavja/$', views.PoglavjeList.as_view(), name='poglavje-list'),
    url(r'^poglavje/(?P<pk>\d+)$', views.PoglavjeDetail.as_view(), name='poglavje-detail'),
    url(r'^specifikacije/$', views.SpecifikacijaList.as_view(), name='specifikacija-list'),
    url(r'^specifikacija/(?P<pk>\d+)$', views.SpecifikacijaDetail.as_view(), name='specifikacija-detail'),
    url(r'^podrobnosti1/$', views.Podrobnost1List.as_view(), name='podrobnost1-list'),
    url(r'^podrobnost1/(?P<pk>\d+)$', views.Podrobnost1Detail.as_view(), name='podrobnost1-detail'),
    url(r'^podrobnosti2/$', views.Podrobnost2List.as_view(), name='podrobnost2-list'),
    url(r'^podrobnost2/(?P<pk>\d+)$', views.Podrobnost2Detail.as_view(), name='podrobnost2-detail'),


]
