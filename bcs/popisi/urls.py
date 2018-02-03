from django.conf.urls import url
from django.views.generic import TemplateView
from . import views


urlpatterns = [

    url(r'^postavke/$', views.PostavkaList.as_view(), name='postavka-list'),
    url(r'^postavka/(?P<pk>\d+)$', views.PostavkaDetail.as_view(), name='postavka-detail'),
    url(r'^dela/$', views.DelaList.as_view(), name='dela-list'),
    url(r'^dela/(?P<pk>\d+)$', views.DelaDetail.as_view(), name='dela-detail'),
    url(r'^vrsta_del/$', views.VrstaDelList.as_view(), name='vrstadel-list'),
    url(r'^vrsta_dela/(?P<pk>\d+)$', views.VrstaDelDetail.as_view(), name='vrstadel-detail'),

]
