
# API de Plataforma de Cursos Online

Este projeto é uma API REST desenvolvida em Python com  **FastAPI** , focada na implementação de uma arquitetura em camadas (Domain, Service, Repository, API). O objetivo principal é a organização clara de responsabilidades e a aplicação de regras de negócio no domínio da aplicação.

## 🚀 Tecnologias Utilizadas

* **Python 3.12**
* **FastAPI** (Framework web)
* **Pydantic** (Validação de dados e Schemas)
* **Uvicorn** (Servidor ASGI)
* **Docker & Docker Compose** (Containerização)

## 🏗️ Estrutura do Projeto

A aplicação segue a organização de pastas definida nos requisitos do projeto:

**Plaintext**

```
cursos_api/
├── src/
│   ├── api/routes/   # Definição dos endpoints
│   ├── domain/       # Entidades e regras de negócio puras
│   ├── schemas/      # Definição de entrada e saída (Pydantic)
│   ├── repositories/ # Camada de acesso a dados (In-memory)
│   ├── services/     # Orquestração e lógica da aplicação
│   └── database/     # Instância do banco de dados em memória
├── main.py           # Ponto de entrada da aplicação
├── Dockerfile
└── docker-compose.yml
```

## ⚖️ Regras de Negócio Implementadas

As regras de precificação foram centralizadas na entidade de domínio `Curso`, garantindo que a lógica não esteja dispersa nas rotas:

1. **Cursos Gratuitos (Tipo 1):** O preço final é sempre  **0** , independentemente do valor base ou desconto.
2. **Cursos Pagos (Tipo 2):** Permitem a aplicação de um desconto percentual sobre o valor base.
3. **Proteção de Valor:** O preço final calculado nunca pode ser negativo.

## 🛠️ Como Executar

Certifique-se de ter o **Docker** instalado em sua máquina.

1. Clone o repositório.
2. Na raiz do projeto, execute o comando:
   **Bash**

   ```
   docker compose up --build
   ```
3. Acesse a documentação interativa (Swagger) em: [http://localhost:8002/docs](https://www.google.com/search?q=http://localhost:8002/docs)

## 📡 Endpoints da API

### Alunos

* `POST /alunos`: Cadastro de novo aluno.
* `GET /alunos`: Listagem de todos os alunos.

### Cursos

* `POST /cursos`: Cadastro de novo curso.
* `GET /cursos`: Listagem de todos os cursos.
* `GET /cursos/{codigo}`: Busca detalhada de um curso.
* `PUT /cursos/{codigo}/preco`: Atualização do preço base de um curso.
* `GET /cursos/{codigo}/preco-final`: Consulta do preço calculado após regras de negócio.

---

## Autor

**Nome Completo:** Lucas Paiva S. de Olieira

**GitHub:** [lucaspaiva-lp](https://github.com/lucaspaiva-lp)
