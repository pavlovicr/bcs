from django.db import models
from django.urls import reverse


#BCS
from osnova.utils import ChoiceEnum
from osnova.models import Osnova


class Zvrst(ChoiceEnum):
    STANDARD = 'Standard'
    TS = 'Tehnična specifikacija'
    TP = 'Tehnični predpis'
    PRAVILNIK = 'Pravilnik'
    ZNANOST = 'Znanostvena knjiga'
    PRAKSA = 'Gradbena praksa'
    SMERNICE = 'Smernice'
    PRIPOROCILA = 'Priporocila'


class Dokumentacija(Osnova):
    naslov = models.TextField(blank=True)
    zvrst = models.CharField(max_length=30, choices=Zvrst.choices(), default=Zvrst.STANDARD)
    komentar = models.TextField()

    def __str__(self):
        return self.opis

    def get_absolute_url(self):
        return reverse('dokumentacija-detail', args=[str(self.id)])


class Slika(Osnova):
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.opis

    def get_absolute_url(self):
        return reverse('slika-detail', args=[str(self.id)])


class Datoteka(Osnova):
    datoteka = models.FileField(blank=True)

    def __str__(self):
        return self.opis

    def get_absolute_url(self):
        return reverse('datoteka-detail', args=[str(self.id)])


class Podrocje(ChoiceEnum):
    MATERIAL = 'Lastnosti materiala'
    IZDELEK = 'Lastnosti izdelka'
    PROCES = 'Delovni postopki'
    VARNOST = 'Varnostne zahteve'
    SPLOSNO = 'Splošno'


#Predmet pove, na kaj se nanaša Podlaga. Primer " sveža betonska mešanica po SIST EN ...."
class Predmet(Osnova):
        podrocje = models.CharField(max_length=10, choices=Podrocje.choices(), default=Podrocje.MATERIAL)

        def __str__(self):
            return self.opis

        def get_absolute_url(self):
            return reverse('predmet-detail', args=[str(self.id)])


#Podlaga, temeljni dokument Podrobnosti.
class Podlaga(Osnova):
    komentar = models.TextField()
    dokumentacija = models.ManyToManyField(Dokumentacija)
    predmet = models.ForeignKey('Predmet', on_delete=models.SET_NULL, null=True)
    slika = models.ManyToManyField(Slika)

    def __str__(self):
        return self.opis

    def get_absolute_url(self):
        return reverse('podlaga-detail', args=[str(self.id)])


class MeriloOsnova(Osnova):

    def __str__(self):
        return self.opis

    def get_absolute_url(self):
        return reverse('meriloosnova-detail', args=[str(self.id)])

class MeriloSkupina1(Osnova):

    def __str__(self):
        return self.opis

    def get_absolute_url(self):
        return reverse('meriloskupina1-detail', args=[str(self.id)])

class Izhodisce(ChoiceEnum):
    ZAKON = 'Zahtevano z zakonom'
    STROKA = 'Pravila stroke'
    PRAKSA = 'Gradbena praksa'
    ZNANOST = 'Znanstvena dognanja'
    ZDRUZENJA = 'Priporočila združenj'
    IZVAJALCI = 'Priporočila izvajalcev'


class Merilo(Osnova):
    merilo_osnova = models.ForeignKey('MeriloOsnova')
    merilo_skupina1 = models.ForeignKey('MeriloSkupina1', on_delete=models.SET_NULL, blank=True, null=True)
    izhodisce = models.CharField(max_length=10, choices=Izhodisce.choices(), default=Izhodisce.STROKA)
    podlaga = models.ForeignKey('Podlaga', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.opis

    def get_absolute_url(self):
        return reverse('merilo-detail', args=[str(self.id)])


class Podrobnost(Osnova):
    merilo = models.ManyToManyField(Merilo)
    komentar = models.TextField(blank=True)

    def __str__(self):
        return self.opis

    def get_absolute_url(self):
        return reverse('podrobnost-detail', args=[str(self.id)])
