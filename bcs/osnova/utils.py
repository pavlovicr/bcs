# to je pythonov modul enum, ki ga uporabimo za izbirne podatke v CHOICES v modelsih
from enum import Enum

class ChoiceEnum(Enum):
    @classmethod
    def choices(cls):
return tuple((x.name,x.value) for x in cls)
