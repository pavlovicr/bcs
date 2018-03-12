from django.db import models
from django.urls import reverse

#bcs
from osnova.utils import ChoiceEnum
from osnova.models import Osnova
from podrobnosti.models import Merilo, Dokumentacija, Podrobnost


class SkupinaDel(ChoiceEnum):
    GRADBENA = 'Gradbena dela'
    OBRTNISKA = 'Obrtniška dela'
    STROJNE = 'Strojne instalacije'
    ELEKTRO = 'Električne instalacije'
    ZUNANJA = 'Zunanja ureditev'


class VrstaDel(Osnova):
    skupina_del = models.CharField(max_length=10, choices=SkupinaDel.choices(), default=SkupinaDel.GRADBENA)

    def __str__(self):
        return self.tekst

    def get_absolute_url(self):
        return reverse('vrstadel-detail', args=[str(self.id)])


class NivoDolocilaDel(ChoiceEnum):
    NIZEK = 'Določila, minimalna vsebina '
    SREDNJI = 'Določila, običajna vsebina'
    VISOK = 'Določila, podrobna vsebina'


class Dela(Osnova):
    vrsta_del = models.ForeignKey('VrstaDel', on_delete=models.SET_NULL, null=True)
    nivo = models.CharField(max_length=10, choices=NivoDolocilaDel.choices(), default=NivoDolocilaDel.SREDNJI)
    predmet = models.TextField(blank=True)
    osnovni_materiali = models.TextField(blank=True)
    osnove_za_izvedbo = models.TextField(blank=True)
    nacin_izvedbe = models.TextField(blank=True)
    kakovost_izvedenih_del = models.TextField(blank=True)
    preverjanje_kakovosti_izvedenih_del = models.TextField(blank=True)
    merjenje_prevzem_obracun = models.TextField(blank=True)
    dokumentacija = models.ManyToManyField((Dokumentacija), blank=True)


    def __str__(self):
        return self.tekst

    def get_absolute_url(self):
        return reverse('dela-detail', args=[str(self.id)])


class Postavka(Osnova):
    enota_mere = models.CharField(max_length=10)
    dela = models.ForeignKey('Dela', on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return self.tekst

    def get_absolute_url(self):
        return reverse('postavka-detail', args=[str(self.id)])


class PopisnaPostavka(Osnova):
    postavka = models.ForeignKey('Postavka', on_delete=models.SET_NULL, null=True)
    podrobnost = models.ManyToManyField('podrobnosti.Podrobnost')

    #@property
    #def abrakadabra(self):
    #    return self.abrakadabra.order_by('komentar')

    def __str__(self):
        return self.tekst

    def get_absolute_url(self):
        return reverse('popisnapostavka-detail', args=[str(self.id)])
