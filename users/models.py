from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

from django.utils import timezone


DISCOUNT_CODE_TYPES_CHOICES = [
    ('percent', 'Percentage-based'),
    ('value', 'Value-based'),
]
def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

class Profil(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=255)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class TypeActivte(models.Model):

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class TypeSpeculation(models.Model):

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    active = models.BooleanField(default=False)
    activite = models.ForeignKey('users.TypeActivte', on_delete=models.SET_NULL, related_name='speculations',null = True)

    def __str__(self):
        return self.name
# Create your models here
class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):
    STATUS_MASCULIN = 'masculin'
    STATUS_FEMININ = 'féminin'

    STATUS_SEXE = (
        (STATUS_MASCULIN,'Masculin'),
        (STATUS_FEMININ,'Féminin'),
    )

    STATUS_VISIBLE = 'En activité'
    STATUS_HIDDEN = 'Au chômage'
    STATUS_OFF = 'Indisponible'

    STATUS_CHOICES = (
        (STATUS_VISIBLE,'En activité'),
        (STATUS_HIDDEN,'Au chômage'),
        (STATUS_OFF,'Indisponible'),
    )
    STATUS_CELIBAT = 'Célibataire'
    STATUS_MARIE = 'Marié(e)'
    STATUS_DIVORCE = 'Divorcé(e)'

    STATUS_SITUATIONS = (
        (STATUS_CELIBAT,'Célibataire'),
        (STATUS_MARIE,'Marié(e)'),
        (STATUS_DIVORCE,'Divorcé(e)'),
    )
    email = models.EmailField(
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    profile = models.CharField(blank=True, null=True,max_length=255)
    credits = models.PositiveIntegerField(default=100)
    linkedin_token = models.TextField(blank=True, default='')
    expiry_date = models.DateTimeField(null=True, blank=True)
    name = models.CharField(max_length=100,null=True, blank=True)
    tel = models.CharField(max_length=100,null=True, blank=True)
    tel2 = models.CharField(max_length=100,null=True, blank=True)
    firstname = models.CharField(max_length=100,null=True, blank=True)
    photo = models.ImageField(upload_to=upload_to, blank=True, null=True)
    pays = models.CharField(max_length=50,null=True, blank=True)
    province = models.CharField(max_length=100,null=True, blank=True)
    village = models.CharField(max_length=100,null=True, blank=True)
    quartier = models.CharField(max_length=100,null=True, blank=True)
    fonction = models.CharField(max_length=100,null=True, blank=True)
    age = models.IntegerField(default=1)
    employes = models.IntegerField(default=1)
    personnes_charge = models.IntegerField(default=0)
    salaire_minimum = models.IntegerField(default=0)
    sexe = models.CharField(default=STATUS_FEMININ,max_length=20,choices=STATUS_SEXE)
    situation = models.CharField(default=STATUS_CELIBAT,max_length=20,choices=STATUS_SITUATIONS)
    longitude = models.CharField(max_length=100,null=True, blank=True)
    latitude = models.CharField(max_length=100,null=True, blank=True)
    zone = models.CharField(max_length=100,null=True, blank=True)
    status = models.CharField(default=STATUS_VISIBLE,max_length=20,choices=STATUS_CHOICES ,null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    profil = models.ForeignKey('users.Profil', on_delete=models.SET_NULL, related_name='users',null = True)
    typeActivte = models.ForeignKey('users.TypeActivte', on_delete=models.SET_NULL, related_name='users',null = True)
    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS = ['date_of_birth']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    @property
    def is_out_of_credits(self):
        "Is the user out  of credits?"
        return self.credits > 0

    @property
    def has_sufficient_credits(self, cost):
        return self.credits - cost >= 0

    @property
    def linkedin_signed_in(self):
        return bool(self.linkedin_token) and self.expiry_date > timezone.now()
