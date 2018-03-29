from django.db import models
from django.urls import reverse

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


class Vir(Osnova):
    naslov = models.TextField(blank=True)
    zvrst = models.CharField(max_length=30, choices=Zvrst.choices(), default=Zvrst.STANDARD)
    komentar = models.TextField(blank=True)
    tekst_file = models.FileField(blank=True)

    def __str__(self):
        return self.tekst

    def get_absolute_url(self):
        return reverse('vir-detail', args=[str(self.id)])


class Namen(Osnova):

    def __str__(self):
        return self.tekst

    def get_absolute_url(self):
        return reverse('namen-detail', args=[str(self.id)])


class Gradivo(Osnova):
    slika = models.ImageField(blank=True)
    tekst_file = models.FileField(blank=True)
    namen = models.ForeignKey('Namen',on_delete=models.SET_NULL, null=True)
    vir = models.ForeignKey('Vir',on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return self.tekst

    def get_absolute_url(self):
        return reverse('gradivo-detail', args=[str(self.id)])


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
    ZAKON = 'Zakonodaja'
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
    gradivo = models.ManyToManyField((Gradivo), blank=True)


    def __str__(self):
        return self.tekst

    def get_absolute_url(self):
        return reverse('specifikacija-detail', args=[str(self.id)])


class Odsek(Osnova):
    tekst_za_popis = models.TextField(blank=True)

    def __str__(self):
        return self.tekst

    def get_absolute_url(self):
        return reverse('segment-detail', args=[str(self.id)])


class Podrobnost(Osnova):
    ''' Nekaj o podrobnostih '''
    odsek = models.ForeignKey('Odsek', on_delete=models.SET_NULL, blank=True, null=True)
    specifikacija = models.ForeignKey('Specifikacija', on_delete=models.SET_NULL, null=True)
    komentar = models.TextField(blank=True)
    tekst_za_popis = models.TextField(blank=True)

    def gsx(self):
        a=str(self.specifikacija.poglavje.dela.vrsta_del.stevilka)
        return a

    # Pazi !, V kolikor ne bo vseh unosov tujih ključev ne dela
    @property
    def gs(self):
        a = str(self.stevilka)
        b = str(self.odsek.stevilka)
        c = str(self.specifikacija.stevilka)
        d = str(self.specifikacija.poglavje.stevilka)
        e = str(self.specifikacija.poglavje.dela.stevilka)
        f = str(self.specifikacija.poglavje.dela.vrsta_del.stevilka)
        return [f,e,d,c,b,a]

    class Meta:
        ordering = ['specifikacija__stevilka','stevilka']


    def __str__(self):
        return self.tekst

    def get_absolute_url(self):
        return reverse('podrobnost-detail', args=[str(self.id)])
