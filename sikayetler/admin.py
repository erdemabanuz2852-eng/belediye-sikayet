from django.contrib import admin
from .models import Birim, Sikayet, Aksiyon

@admin.register(Birim)
class BirimAdmin(admin.ModelAdmin):
    list_display = ('isim',)
    search_fields = ('isim',)

def durumu_cozuldu_yap(modeladmin, request, queryset):
    queryset.update(durum='Çözüldü')
durumu_cozuldu_yap.short_description = "Seçili şikayetleri 'Çözüldü' yap"

@admin.register(Sikayet)
class SikayetAdmin(admin.ModelAdmin):
    list_display = ('baslik','durum','ilgili_birim','olusturan_kullanici','olusturma_tarihi')
    list_filter = ('durum','ilgili_birim','olusturma_tarihi')
    search_fields = ('baslik','aciklama')
    raw_id_fields = ('olusturan_kullanici',)
    date_hierarchy = 'olusturma_tarihi'
    actions = [durumu_cozuldu_yap]

@admin.register(Aksiyon)
class AksiyonAdmin(admin.ModelAdmin):
    list_display = ('sikayet','yapan_kullanici','tarih')
    list_filter = ('sikayet','yapan_kullanici')
    search_fields = ('aciklama',)
