from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from activite.models import Activite,Etape,Vente,Rendement
from activite.serializers import ActiviteSerializer,EtapeSerializer, VenteSerializer,ImageEtapeSerializer,RendementSerializer

# Create your views here.
class VenteAPIView(APIView):
    def get(self, *args, **kwargs):
        articles = Vente.objects.all()
        serializer = VenteSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VenteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RendementAPIView(APIView):
    def get(self, *args, **kwargs):
        articles = Rendement.objects.all()
        serializer = RendementSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RendementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class EtapeAPIView(APIView):
    def get(self, *args, **kwargs):
        articles = Etape.objects.all()
        serializer = EtapeSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        instance_data = request.data
        data = {key: value for key, value in instance_data.items()}
        serializer = EtapeSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()

        if request.FILES:
            photos = dict((request.FILES).lists()).get('images', None)
            if photos:
                for photo in photos:
                    photo_data = {}
                    photo_data["etape"] = instance.pk
                    photo_data["image"] = photo
                    photo_serializer = ImageEtapeSerializer(data=photo_data)
                    photo_serializer.is_valid(raise_exception=True)
                    photo_serializer.save()

        return Response(serializer.data)
        
class ActiviteViewSet(ModelViewSet):
    serializer_class = ActiviteSerializer
    queryset = Activite.objects.all()

    def get_queryset(self):
        articles = Activite.objects.all()
        user_id = self.request.GET.get('user_id')
        if user_id is not None:
            articles = articles.filter(user_id = user_id)
        return articles
