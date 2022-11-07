from rest_framework import serializers

from activite.models import Etape,ImageEtape,Activite,Vente

class ImageEtapeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageEtape
        fields = ['id', 'image','etape']

class VenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vente
        fields = ['id','depenses','benefices','etape','vente','date_created']

class EtapeSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    ventes = serializers.SerializerMethodField()

    class Meta:
        model = Etape
        fields = ['id', 'libelle','description','activite','images','ventes']

    def get_images(self,instance):
        queryset = ImageEtape.objects.filter(etape=instance)
        serializer = ImageEtapeSerializer(queryset, many=True)
        return serializer.data
    
    def get_ventes(self,instance):
        queryset = Vente.objects.filter(etape=instance)
        serializer = VenteSerializer(queryset, many=True)
        return serializer.data

    
class ActiviteSerializer(serializers.ModelSerializer):
    etapes = serializers.SerializerMethodField()

    class Meta:
        model = Activite
        fields = ['id', 'libelle','description','user','typeactivite','speculation','longitude','latitude','statut','date_debut','date_fin','etapes']

    def get_etapes(self,instance):
        queryset = Etape.objects.filter(activite=instance)
        serializer = EtapeSerializer(queryset, many=True)
        return serializer.data

