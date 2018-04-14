from django import forms
class ImeForm(forms.Form):
    ime=forms.CharField(label ='Tvoje ime', max_length=6,initial='hihi')
