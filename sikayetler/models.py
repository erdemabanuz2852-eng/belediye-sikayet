from django.db import models
from django.contrib.auth.models import User

class Birim(models.Model):
    isim = models.CharField(max_length=100)
    aciklama = models.TextField(blank=True, null=True)
    def __str__(self): return self.isim

class Sikayet(models.Model):
    baslik = models.CharField(max_length=200)
    aciklama = models.TextField()
    DURUM_SECENEKLERI = [('Yeni','Yeni'),('Yönlendirildi','Yönlendirildi'),
                         ('İşlemde','İşlemde'),('Çözüldü','Çözüldü'),('Reddedildi','Reddedildi')]
    durum = models.CharField(max_length=20, choices=DURUM_SECENEKLERI, default='Yeni')
    ilgili_birim = models.ForeignKey(Birim, on_delete=models.SET_NULL, null=True, related_name='sikayetler')
    olusturan_kullanici = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    olusturma_tarihi = models.DateTimeField(auto_now_add=True)
    guncelleme_tarihi = models.DateTimeField(auto_now=True)
    dosya = models.FileField(upload_to='sikayet_dosyalari/', blank=True, null=True)
    def __str__(self): return self.baslik

class Aksiyon(models.Model):
    sikayet = models.ForeignKey(Sikayet, on_delete=models.CASCADE, related_name='aksiyonlar')
    yapan_kullanici = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    aciklama = models.TextField()
    tarih = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.sikayet.baslik} - {self.tarih.strftime('%Y-%m-%d %H:%M')}"
