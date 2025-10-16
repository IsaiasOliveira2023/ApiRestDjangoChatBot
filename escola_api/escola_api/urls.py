# escola_api/urls.py

from django.contrib import admin
from django.urls import path, include
# ⬅️ IMPORTAR A VIEW DIRETO DO APP MATERIAS
from materias.views import pagina_reserva 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('materias.urls')),
    # ⬅️ NOVA ROTA: CHAMA A FUNÇÃO DIRETAMENTE
    path('reserva/', pagina_reserva, name='reserva'), 
]