from django.db import models

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)
# Create your models here.
class Activite(models.Model):
    date_debut = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_fin = models.DateTimeField(null=True,blank=True)

    libelle = models.CharField(max_length=255)
    statut = models.CharField(max_length=50)
    longitude = models.CharField(max_length=255)
    latitude = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    active = models.BooleanField(default=False)
    typeactivite = models.ForeignKey('users.TypeActivte',on_delete=models.SET_NULL,related_name='types',null=True)
    speculation = models.ForeignKey('users.TypeSpeculation',on_delete=models.SET_NULL,related_name='speculations',null=True)


    def __str__(self):
        return self.libelle

class Etape(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)

    libelle = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    active = models.BooleanField(default=False)
    activite = models.ForeignKey('activite.Activite',on_delete=models.CASCADE,related_name='etapes')


    def __str__(self):
        return self.libelle

class ImageEtape(models.Model):
    image = models.ImageField(upload_to=upload_to)
    etape = models.ForeignKey('activite.Etape', on_delete=models.CASCADE, related_name='images')

class Vente(models.Model):
    benefices = models.IntegerField()
    depenses = models.IntegerField()
    vente = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    etape = models.ForeignKey('activite.Etape', on_delete=models.CASCADE, related_name='ventes')
