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
        return self.tekst

    def get_absolute_url(self):
        return reverse('dokumentacija-detail', args=[str(self.id)])


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


class Podrocje(ChoiceEnum):
    MATERIAL = 'Lastnosti materiala'
    IZDELEK = 'Lastnosti izdelka'
    PROCES = 'Delovni postopki'
    VARNOST = 'Varnostne zahteve'
    SPLOSNO = 'Splošno'


class PredmetMerila(Osnova):
        dela = models.ForeignKey('popisi.Dela',on_delete=models.SET_NULL, null=True)
        podrocje = models.CharField(max_length=10, choices=Podrocje.choices(), default=Podrocje.MATERIAL)

        def __str__(self):
            return self.tekst

        def get_absolute_url(self):
            return reverse('predmetmerila-detail', args=[str(self.id)])


class Izhodisce(ChoiceEnum):
    ZAKON = 'Zahtevano z zakonom'
    STROKA = 'Pravila stroke'
    PRAKSA = 'Gradbena praksa'
    ZNANOST = 'Znanstvena dognanja'
    ZDRUZENJA = 'Priporočila združenj'
    IZVAJALCI = 'Priporočila izvajalcev'


class PodlagaMerila(Osnova):
    predmet_merila = models.ForeignKey('PredmetMerila', on_delete=models.SET_NULL, null=True)
    izhodisce = models.CharField(max_length=10, choices=Izhodisce.choices(), default=Izhodisce.STROKA)
    komentar = models.TextField()
    dokumentacija = models.ManyToManyField((Dokumentacija), blank=True)
    slika = models.ManyToManyField((Slika), blank=True )

    def __str__(self):
        return self.tekst

    def get_absolute_url(self):
        return reverse('podlagamerila-detail', args=[str(self.id)])


class Merilo(Osnova):
    podlaga_merila = models.ForeignKey('PodlagaMerila', on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        ordering = ['stevilka']

    def __str__(self):
        return self.tekst

    def get_absolute_url(self):
        return reverse('merilo-detail', args=[str(self.id)])


class Podrobnost(Osnova):
    merilo =  models.ForeignKey('Merilo', on_delete=models.SET_NULL, null=True)
    tekst_za_popis = models.TextField(blank=True)

    class Meta:
        ordering = ['merilo__stevilka']

    def __str__(self):
        return self.tekst

    def get_absolute_url(self):
        return reverse('podrobnost-detail', args=[str(self.id)])
