from rest_framework import serializers
from users.models import MyUser,TypeActivte,Profil,TypeSpeculation
from activite.models import Activite
from activite.serializers import ActiviteSerializer


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)
    photo = serializers.ImageField(required=False)

    class Meta:
        model = MyUser
        fields = ['id','email', 'password', 'password2','name','profil','typeActivte','photo',
        'pays','firstname','village','quartier','tel','tel2','age','employes','sexe','situation',
        'longitude','latitude','zone','status','fonction','salaire_minimum','personnes_charge']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = MyUser(
            email=self.validated_data.get('email'), 
            date_of_birth=self.validated_data.get('date_of_birth',),
            name = self.validated_data.get('name','Pas de nom'),
            firstname = self.validated_data.get('firstname','Pas de prénom'),
            pays = self.validated_data.get('pays',),
            village = self.validated_data.get('village',),
            quartier = self.validated_data.get('quartier',),
            tel = self.validated_data.get('tel'),
            tel2 = self.validated_data.get('tel2'),
            age = self.validated_data.get('age',18),
            employes = self.validated_data.get('employes',0),
            sexe = self.validated_data.get('sexe','Masculin'),
            situation = self.validated_data.get('situation','Célibataire'),
            longitude = self.validated_data.get('longitude',),
            latitude = self.validated_data.get('latitude',),
            personnes_charge = self.validated_data.get('personnes_charge',0),
            salaire_minimum = self.validated_data.get('salaire_minimum',0),
            fonction = self.validated_data.get('fonction'),
            zone = self.validated_data.get('zone',),
            status = self.validated_data.get('status','Au chômage'),
            profil = self.validated_data.get('profil'),
            typeActivte = self.validated_data.get('typeActivte'),
            photo = self.validated_data.pop('photo')
            )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        user.set_password(password)
        user.save()
        return user


class PasswordChangeSerializer(serializers.Serializer):
    current_password = serializers.CharField(style={"input_type": "password"}, required=True)
    new_password = serializers.CharField(style={"input_type": "password"}, required=True)

    def validate_current_password(self, value):
        if not self.context['request'].user.check_password(value):
            raise serializers.ValidationError({'current_password': 'Does not match'})
        return value

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profil
        fields = ['id','name']

class TypeActiviteSerializer(serializers.ModelSerializer):
    speculations = serializers.SerializerMethodField()
    class Meta:
        model = TypeActivte
        fields = ['id','name','speculations']

    def get_speculations(self,instance):
        queryset = TypeSpeculation.objects.filter(activite=instance)
        serializer = TypeSpeculationSerializer(queryset, many=True)

        return serializer.data

class TypeSpeculationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeSpeculation
        fields = ['id','name']

class UserSerializer(serializers.ModelSerializer):
    activites = serializers.SerializerMethodField()
    class Meta:
        model = MyUser
        fields = ['id','email','name','firstname','tel','photo','pays','province','village','quartier','age',
        'employes','sexe','situation','longitude','latitude','zone','status','profil','typeActivte','personnes_charge','fonction','activites']
    
    def get_activites(self,instance):
        queryset = Activite.objects.filter(user=instance)
        serializer = ActiviteSerializer(queryset, many=True)
        return serializer.data