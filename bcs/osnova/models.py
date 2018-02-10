from django.db import models

# polje "opis" za vse modelsa popii,podrobnosti
class Osnova(models.Model):
    opis = models.CharField(max_length=100)

    class Meta:
        abstract = True
