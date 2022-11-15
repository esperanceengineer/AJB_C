from blog.models import Article, Temoignage, Partenaire, Sujet, Comment, Image
from users.serializers import TypeActiviteSerializer,UserSerializer
from rest_framework import serializers


class ArticleSerializer(serializers.ModelSerializer):
    #image = serializers.ImageField(require=False)
    class Meta:
        model = Article
        fields = ['id', 'date_created', 'date_updated','name','description','image']

class PartenaireSerializer(serializers.ModelSerializer):
    #image = serializers.ImageField(require=False)
    class Meta:
        model = Partenaire
        fields = ['id', 'date_created', 'date_updated','name','image']


class TemoignageSerializer(serializers.ModelSerializer):
    #image = serializers.ImageField(require=False)
    class Meta:
        model = Temoignage
        fields = ['id','title', 'date_created', 'date_updated','author','description','photo']

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'image','sujet']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'author_name','sujet','text']

class SujetSerialiazer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)
    activite = TypeActiviteSerializer(many=False)
    user = UserSerializer(many=False)
    class Meta:
        model = Sujet
        fields = ['id','title','activite','user','text','created_at','image']

class SujetDetailSerialiazer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Sujet
        fields = ['id','title','activite','user','text','created_at','images','comments']

    def get_images(self,instance):
        queryset = Image.objects.filter(sujet=instance)
        serializer = ImageSerializer(queryset, many=True)

        return serializer.data

    def get_comments(self,instance):
        queryset = Comment.objects.filter(sujet=instance)
        serializer = CommentSerializer(queryset, many=True)

        return serializer.data