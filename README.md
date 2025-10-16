📚 Projeto Escola API & Chatbot de Reservas
Este projeto implementa uma API RESTful simples para gerenciar matérias de uma escola, utilizando Django REST Framework (DRF), e um Frontend Chatbot que interage com essa API para simular a reserva de um laboratório.

🚀 Como Inicializar o Projeto (Passo a Passo)
Siga estas instruções para configurar e rodar o projeto localmente.

1. Acessar o Diretório
Assumindo que você está no diretório onde o ambiente virtual (venv) e a pasta do projeto (escola_api) estão localizados:

Bash

# Entra na pasta do projeto Django
cd escola_api 
2. Ativar o Ambiente Virtual
É crucial ativar o ambiente virtual para garantir que as bibliotecas (django, djangorestframework) estejam acessíveis.

Bash

# Para Windows PowerShell:
..\venv\Scripts\Activate
💡 Após a ativação, você deve ver (venv) no início da linha de comando, indicando que o ambiente está ativo.

3. Rodar as Migrações
Garanta que as tabelas do banco de dados (incluindo o modelo Materia) estejam criadas:

Bash

# Aplica as migrações no banco de dados
python manage.py migrate
4. Iniciar o Servidor
Inicie o servidor de desenvolvimento do Django:

Bash

python manage.py runserver
O servidor estará rodando em: http://127.0.0.1:8000/

🛠️ Endpoints e Testes
O projeto oferece dois endpoints principais: a API REST e a interface do Chatbot.

1. API REST (CRUD de Matérias)
Acesse a interface de teste do DRF (navegador ou Postman) para manipular os dados.

Link: http://127.0.0.1:8000/api/materias/

Método	URL	Descrição
GET	/api/materias/	Lista todas as matérias cadastradas.
POST	/api/materias/	Cria uma nova matéria.
PUT/PATCH	/api/materias/{id}/	Atualiza uma matéria (usando o ID).
DELETE	/api/materias/{id}/	Remove uma matéria.

Exportar para as Planilhas
Exemplo de POST (cURL):

Bash

curl -X POST http://127.0.0.1:8000/api/materias/ \
-H "Content-Type: application/json" \
-d '{"nome": "Programação Web", "professor": "Isaias", "carga_horaria": 80}'
2. Frontend Chatbot de Reservas
Acesse a interface HTML do chatbot que interage com a API:

Link: http://127.0.0.1:8000/reserva/
