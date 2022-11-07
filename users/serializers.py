from rest_framework import serializers
from users.models import MyUser,TypeActivte,Profil


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)
    photo = serializers.ImageField(required=False)

    class Meta:
        model = MyUser
        fields = ['id','email', 'password', 'password2','name','profil','typeActivte','photo',
        'pays','firstname','village','quartier','tel','tel2','age','employes','sexe','situation',
        'longitude','latitude','zone','status']
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
            quartier = self.validated_data.get('village',),
            tel = self.validated_data.get('tel'),
            tel2 = self.validated_data.get('tel2'),
            age = self.validated_data.get('age',18),
            employes = self.validated_data.get('employes',0),
            sexe = self.validated_data.get('sexe','Masculin'),
            situation = self.validated_data.get('situation','Célibataire'),
            longitude = self.validated_data.get('longitude',),
            latitude = self.validated_data.get('latitude',),
            zone = self.validated_data.get('zone',),
            status = self.validated_data.get('status','Au chômage'),
            profil = self.validated_data.get('profil',1),
            typeActivte = self.validated_data.get('typeActivte',1),
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
    class Meta:
        model = TypeActivte
        fields = ['id','name']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = '__all__'