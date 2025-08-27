from django import forms
from .models import Sikayet, Aksiyon

class SikayetForm(forms.ModelForm):
    class Meta:
        model = Sikayet
        fields = ['baslik','aciklama','ilgili_birim','dosya']

class AksiyonForm(forms.ModelForm):
    class Meta:
        model = Aksiyon
        fields = ['aciklama']
