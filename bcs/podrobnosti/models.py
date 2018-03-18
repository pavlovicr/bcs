from django.db import models
from django.urls import reverse

from osnova.utils import ChoiceEnum
from osnova.models import Osnova


class Slika(Osnova):
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.tekst

    def get_absolute_url(self):
        return reverse('slika-detail', args=[str(self.id)])


class Datoteka(Osnova):
    datoteka = models.FileField(blank=True)

    def __str__(self):
        return self.tekst

    def get_absolute_url(self):
        return reverse('datoteka-detail', args=[str(self.id)])


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
    komentar = models.TextField(blank=True)
    image = models.ManyToManyField((Slika), blank=True)
    datoteka = models.ManyToManyField((Datoteka), blank=True)

    def __str__(self):
        return self.tekst

    def get_absolute_url(self):
        return reverse('dokumentacija-detail', args=[str(self.id)])


class Predmet(ChoiceEnum):
    MATERIAL = 'Lastnosti materiala'
    IZDELEK = 'Lastnosti izdelka'
    PROCES = 'Opis delovnih postopkov'
    VARNOST = 'Varnostne zahteve'
    SPLOSNO = 'Splošno'


class Poglavje(Osnova):
        dela = models.ForeignKey('popisi.Dela',on_delete=models.SET_NULL, null=True)
        predmet = models.CharField(max_length=10, choices=Predmet.choices(), default=Predmet.MATERIAL)

        class Meta:
            ordering = ['stevilka']

        def __str__(self):
            return self.tekst

        def get_absolute_url(self):
            return reverse('poglavje-detail', args=[str(self.id)])


class Podlaga(ChoiceEnum):
    ZAKON = 'Zahtevano z zakonom'
    STROKA = 'Pravila stroke'
    PRAKSA = 'Gradbena praksa'
    ZNANOST = 'Znanstvena dognanja'
    ZDRUZENJA = 'Priporočila združenj'
    IZVAJALCI = 'Priporočila izvajalcev'


class Tip(ChoiceEnum):
    POPIS = 'Popis'
    DOLOCILO = 'Dolocilo'


class Specifikacija(Osnova):
    tip = models.CharField(max_length=10, choices=Tip.choices(), default=Tip.POPIS)
    podlaga = models.CharField(max_length=10, choices=Podlaga.choices(), default=Podlaga.STROKA)
    poglavje = models.ForeignKey('Poglavje', on_delete=models.SET_NULL, null=True)
    komentar = models.TextField(blank=True)
    dokumentacija = models.ManyToManyField((Dokumentacija), blank=True)

    def __str__(self):
        return self.tekst

    def get_absolute_url(self):
        return reverse('specifikacija-detail', args=[str(self.id)])


class Podskupina(Osnova):

    def __str__(self):
        return self.tekst

    def get_absolute_url(self):
        return reverse('podskupina-detail', args=[str(self.id)])


class Podrobnost(Osnova):
    podskupina =  models.ForeignKey('Podskupina', on_delete=models.SET_NULL, blank=True, null=True)
    specifikacija = models.ForeignKey('Specifikacija', on_delete=models.SET_NULL, null=True)
    tekst_za_popis = models.TextField(blank=True)

    class Meta:
        ordering = ['specifikacija__stevilka']

    def __str__(self):
        return self.tekst

    def get_absolute_url(self):
        return reverse('podrobnost-detail', args=[str(self.id)])
