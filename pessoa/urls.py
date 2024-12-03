from rest_framework.routers import DefaultRouter
from cadastro.views import PessoaFisicaViewSet
from django.contrib import admin
from django.urls import path, include

router = DefaultRouter()
router.register(r'pessoas', PessoaFisicaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

]