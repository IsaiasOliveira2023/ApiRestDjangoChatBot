# materias/views.py

from rest_framework import viewsets
from django.shortcuts import render # Importação adicionada para renderizar o HTML
from .models import Materia
from .serializers import MateriaSerializer

# 1. View da API (para GET, POST, PUT, DELETE)
class MateriaViewSet(viewsets.ModelViewSet):
    queryset = Materia.objects.all()
    serializer_class = MateriaSerializer

# 2. View do Frontend (para carregar a página do Chatbot)
def pagina_reserva(request):
    return render(request, 'materias/laboratorio.html')