from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from blog.models import Article, Temoignage, Partenaire,Comment,Sujet,Image
from blog.serializers import ArticleSerializer, PartenaireSerializer, TemoignageSerializer, CommentSerializer,SujetSerialiazer, ImageSerializer,SujetDetailSerialiazer
# Create your views here.

class ArticleAPIView(APIView):
    def get(self, *args, **kwargs):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)


class PartenaireAPIView(APIView):
    def get(self, *args, **kwargs):
        articles = Partenaire.objects.all()
        serializer = PartenaireSerializer(articles, many=True)
        return Response(serializer.data)

class TemoignageAPIView(APIView):
    def get(self, *args, **kwargs):
        articles = Temoignage.objects.all()
        serializer = TemoignageSerializer(articles, many=True)
        return Response(serializer.data)

class MultipleSerializerMixin:
    detail_serializer_class = None

    #récupère le serialize spécifique
    def get_serializer_class(self):
        if self.action == 'retrieve' and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        return super().get_serializer_class()

class SujetViewSet(MultipleSerializerMixin,ModelViewSet):
    serializer_class = SujetSerialiazer
    detail_serializer_class = SujetDetailSerialiazer
    queryset = Sujet.objects.all()

    def create(self, request, *args, **kwargs):
        instance_data = request.data
        data = {key: value for key, value in instance_data.items()}
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()

        if request.FILES:
            photos = dict((request.FILES).lists()).get('images', None)
            if photos:
                for photo in photos:
                    photo_data = {}
                    photo_data["sujet"] = instance.pk
                    photo_data["image"] = photo
                    photo_serializer = ImageSerializer(data=photo_data)
                    photo_serializer.is_valid(raise_exception=True)
                    photo_serializer.save()

        return Response(serializer.data)

class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()