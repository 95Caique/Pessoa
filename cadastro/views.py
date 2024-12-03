from rest_framework.viewsets import ModelViewSet
from .models import PessoaFisica
from .serializers import PessoaFisicaSerializer

class PessoaFisicaViewSet(ModelViewSet):
    queryset = PessoaFisica.objects.all()
    serializer_class = PessoaFisicaSerializer