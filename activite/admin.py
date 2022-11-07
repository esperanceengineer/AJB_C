from django.contrib import admin
from activite.models import Activite,Etape,Vente

# Register your models here.
@admin.register(Activite)
class ActiviteAdmin(admin.ModelAdmin):
    list_display = ('id','libelle', 'statut','date_debut','date_fin')

@admin.register(Etape)
class EtapeAdmin(admin.ModelAdmin):
    list_display = ('id','libelle', 'activite','date_created')

@admin.register(Vente)
class VenteAdmin(admin.ModelAdmin):
    list_display = ('vente','benefices', 'depenses','date_created')