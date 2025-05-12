# Backend do Quiz (Baseado em SQLite)

Este documento fornece uma visão geral e instruções para configurar e executar o backend em Python (Flask) para o projeto de Quiz, baseado nos arquivos `bd.py`, `tentativas.py`, `questao.py` e `perguntas.py` fornecidos.

## 1. Visão Geral do Projeto

O backend serve como uma API REST para um aplicativo de quiz. Ele lida com:
*   Autenticação de usuários (registro e login).
*   Gerenciamento de questões (adicionar, listar, buscar por ID, verificar resposta).
*   Registro e consulta de tentativas dos usuários.

Utiliza Flask como framework web e SQLite como banco de dados, conforme definido em `bd.py`.

## 2. Estrutura do Projeto

O projeto está organizado da seguinte forma:

```
/quiz_backend_sqlite
|-- /app                    # Contém a lógica principal da aplicação Flask
|   |-- /routes             # Define os blueprints para as rotas da API
|   |   |-- auth.py         # Rotas de autenticação
|   |   |-- questao.py      # Rotas para gerenciamento de questões
|   |   |-- tentativas.py   # Rotas para gerenciamento de tentativas
|   |-- /utils              # Utilitários
|   |   |-- db.py           # Funções de inicialização e acesso ao banco de dados SQLite
|   |-- __init__.py         # Inicializa a aplicação Flask e registra os blueprints
|-- /venv                   # Ambiente virtual Python (a ser criado)
|-- config.py               # Configurações da aplicação (chaves secretas, nome do banco)
|-- run.py                  # Ponto de entrada para executar a aplicação Flask
|-- requirements.txt        # Lista de dependências Python do projeto
|-- quizDB.db               # Arquivo do banco de dados SQLite (criado na primeira execução)
|-- README.md               # Este arquivo
```

## 3. Instruções de Configuração

Siga os passos abaixo para configurar o ambiente de desenvolvimento:

### 3.1. Pré-requisitos

*   **Python 3.11 ou superior:** Certifique-se de que o Python está instalado.
*   **SQLite3:** Geralmente já vem instalado com o Python.

### 3.2. Ambiente Virtual e Dependências

1.  **Navegue até o diretório do projeto:**
    ```bash
    cd /home/ubuntu/quiz_backend_sqlite
    ```

2.  **Crie um ambiente virtual Python:**
    ```bash
    python3.11 -m venv venv
    ```

3.  **Ative o ambiente virtual:**
    ```bash
    source venv/bin/activate
    ```

4.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

### 3.3. Configuração de Variáveis de Ambiente (Opcional)

O arquivo `config.py` carrega algumas configurações. Para maior segurança, as chaves `SECRET_KEY` e `JWT_SECRET_KEY` podem ser definidas em um arquivo `.env` na raiz do projeto (`/home/ubuntu/quiz_backend_sqlite/.env`):

```env
SECRET_KEY=\"sua_chave_secreta_aqui\"
JWT_SECRET_KEY=\"sua_outra_chave_secreta_aqui\"
```
Se não definidas, chaves aleatórias serão geradas em tempo de execução (não recomendado para produção).

## 4. Executando a Aplicação

Com o ambiente virtual ativado e as dependências instaladas:

1.  **Inicie o servidor Flask:**
    ```bash
    python run.py
    ```

O servidor estará rodando em `http://127.0.0.1:5000/` (ou `http://0.0.0.0:5000/` para acesso na rede local). O banco de dados `quizDB.db` será criado automaticamente no diretório raiz do projeto na primeira execução, com as tabelas definidas em `app/utils/db.py` (baseado no seu `bd.py`).

## 5. Endpoints da API

A API está versionada sob os seguintes prefixos:
*   `/api/auth`
*   `/api/questoes`
*   `/api/tentativas`

### 5.1. Autenticação (`/api/auth`)

*   **Registrar Novo Usuário**
    *   **Método:** `POST`
    *   **URL:** `/register`
    *   **Corpo da Requisição (JSON):** `{"nickname": "seu_nick", "senha": "sua_senha"}`
    *   **Resposta de Sucesso (201):** `{"message": "Usuário registrado com sucesso!", "ID_usuario": <id>}`

*   **Login de Usuário**
    *   **Método:** `POST`
    *   **URL:** `/login`
    *   **Corpo da Requisição (JSON):** `{"nickname": "seu_nick", "senha": "sua_senha"}`
    *   **Resposta de Sucesso (200):** `{"access_token": "<token_jwt>", "ID_usuario": <id>, "nickname": "seu_nick"}`

### 5.2. Gerenciamento de Questões (`/api/questoes`)

*   **Adicionar Nova Questão**
    *   **Método:** `POST`
    *   **URL:** `/`
    *   **Requer Autenticação (Bearer Token JWT).**
    *   **Corpo da Requisição (JSON):** `{"enunciado": "...", "alternativaA": "...", ..., "resposta_correta": "A", "dica": "...", "valor": 100, "nivel_dificuldade": "Fácil"}`
    *   **Resposta de Sucesso (201):** `{"message": "Questão adicionada com sucesso!", "ID_questao": <id>}`

*   **Listar Todas as Questões**
    *   **Método:** `GET`
    *   **URL:** `/`
    *   **Resposta de Sucesso (200):** Lista de objetos de questão.

*   **Buscar Questão por ID**
    *   **Método:** `GET`
    *   **URL:** `/<int:id_questao>`
    *   **Resposta de Sucesso (200):** Objeto da questão. 404 se não encontrada.

*   **Verificar Resposta**
    *   **Método:** `POST`
    *   **URL:** `/check_answer`
    *   **Requer Autenticação (Bearer Token JWT).**
    *   **Corpo da Requisição (JSON):** `{"id_questao": <id>, "resposta_usuario": "A"}`
    *   **Resposta de Sucesso (200):** `{"correto": true/false}`. 404 se questão não encontrada.

### 5.3. Gerenciamento de Tentativas (`/api/tentativas`)

*   **Registrar Nova Tentativa**
    *   **Método:** `POST`
    *   **URL:** `/`
    *   **Requer Autenticação (Bearer Token JWT).**
    *   **Corpo da Requisição (JSON):** `{"valor_total": <pontos>}`
    *   **Resposta de Sucesso (201):** `{"message": "Tentativa registrada com sucesso!", "ID_tentativa": <id>}`

*   **Buscar Tentativas do Usuário Autenticado**
    *   **Método:** `GET`
    *   **URL:** `/minhas`
    *   **Requer Autenticação (Bearer Token JWT).**
    *   **Resposta de Sucesso (200):** Lista de objetos de tentativa do usuário.

## 6. Considerações

*   Este backend foi criado estritamente com base nos arquivos Python fornecidos. A lógica de `perguntas.py` (dados estáticos) não foi diretamente incorporada, pois o sistema agora depende do banco de dados para armazenar e gerenciar questões.
*   A segurança das senhas é feita com hash usando `werkzeug.security`.
*   A autenticação de API é feita com `Flask-JWT-Extended`.

---

Este README fornece as informações essenciais para começar a trabalhar com o backend do Quiz. Consulte o código-fonte para detalhes mais aprofundados sobre a implementação.
