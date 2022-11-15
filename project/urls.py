"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,include
from django.contrib import admin
from users.views import RegistrationView, LoginView, LogoutView,ChangePasswordView
from rest_framework_simplejwt import views as jwt_views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

from blog.views import ArticleAPIView,ArticleDetailAPIView,PartenaireAPIView,TemoignageAPIView, SujetViewSet,CommentViewSet
from users.views import ProfilAPIView,TypeActiviteAPIView,UserAPIView, UserDetailAPIView
from activite.views import VenteAPIView,ActiviteViewSet,EtapeAPIView,RendementAPIView

router = routers.DefaultRouter()
router.register('sujet',SujetViewSet, basename='sujet')
router.register('comment',CommentViewSet,basename='comment')
router.register('activite',ActiviteViewSet,basename='activite')




#app_name = 'users'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/article', ArticleAPIView.as_view()),
    path('api/article/<int:pk>', ArticleDetailAPIView.as_view()),
    path('api/partenaire', PartenaireAPIView.as_view()),
    path('api/temoignage', TemoignageAPIView.as_view()),
    path('api/typeactivite', TypeActiviteAPIView.as_view()),
    path('api/profils', ProfilAPIView.as_view()),
    path('api/vente/', VenteAPIView.as_view()),
    path('api/rendement/', RendementAPIView.as_view()),
    path('api/etape/', EtapeAPIView.as_view()),
    path('api/users', UserAPIView.as_view()),
    path('api/users/<int:pk>', UserDetailAPIView.as_view()),
    path('accounts/register', RegistrationView.as_view(), name='register'),
    path('accounts/login', LoginView.as_view(), name='register'),
    path('accounts/logout', LogoutView.as_view(), name='register'),
    path('accounts/change-password', ChangePasswordView.as_view(), name='register'),
    path('accounts/token-refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)