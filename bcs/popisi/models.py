from django.db import models
from django.urls import reverse

from osnova.utils import ChoiceEnum
from osnova.models import Osnova
from podrobnosti.models import  Podrobnost1


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


class Dela(Osnova):
    vrsta_del = models.ForeignKey('VrstaDel', on_delete=models.SET_NULL, null=True)

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
    podrobnost1 = models.ManyToManyField('podrobnosti.Podrobnost1')
    podrobnost2 = models.ManyToManyField('podrobnosti.Podrobnost2')

    def hec(self):
        return self.podrobnost1.all(),self.podrobnost2.all()
    hec = property(hec)




    def __str__(self):
        return self.tekst

    def get_absolute_url(self):
        return reverse('popisnapostavka-detail', args=[str(self.id)])
