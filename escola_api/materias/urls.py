# materias/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MateriaViewSet 
# ⬅️ REMOVEMOS A IMPORTAÇÃO DE 'pagina_reserva' POIS ELA VAI NO ARQUIVO PRINCIPAL

router = DefaultRouter()
# Rota da API REST (mantém apenas 'materias' aqui)
router.register(r'materias', MateriaViewSet) 

urlpatterns = [
    # Apenas as URLs REST (que são todas as rotas do router)
    path("", include(router.urls)),
]