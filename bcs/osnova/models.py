from django.db import models

# polje "opis" za vse modelse popisi,podrobnosti
class Osnova(models.Model):
    stevilka = models.IntegerField(blank=True,null=True)
    tekst = models.CharField(max_length=500)

    class Meta:
        abstract = True
