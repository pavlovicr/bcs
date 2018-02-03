from django.db import models
from django.urls import reverse

#bcs
from osnova.utils import ChoiceEnum
from osnova.models import Osnova

class VrstaDel(Osnova):

    class SkupinaDel(ChoiceEnum):
        GRADBENA = 'Gradbena dela'
        OBRTNISKA = 'Obrtniška dela'
        STROJNE = 'Strojne instalacije'
        ELEKTRO = 'Električne instalacije'
        ZUNANJA = 'Zunanja ureditev'
        
    skupina_del = models.CharField(max_length=10, choices=SkupinaDel.choices(), default=SkupinaDel.GRADBENA)

    def __str__(self):
        return self.opis

    def get_absolute_url(self):
        return reverse('vrstadel-detail', args=[str(self.id)])


class Dela(Osnova):
    vrsta_del = models.ForeignKey('VrstaDel', on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.opis

    def get_absolute_url(self):
        return reverse('dela-detail', args=[str(self.id)])


class Postavka(Osnova):
    enota_mere = models.CharField(max_length=10)
    dela = models.ForeignKey('Dela', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.opis
    def get_absolute_url(self):
return reverse('postavka-detail', args=[str(self.id)])
